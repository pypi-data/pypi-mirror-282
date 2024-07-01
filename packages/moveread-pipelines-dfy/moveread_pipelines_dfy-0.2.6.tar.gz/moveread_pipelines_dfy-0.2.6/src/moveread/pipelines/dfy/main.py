import os

LOAD_DOTENV = os.getenv('LOAD_DOTENV')
if LOAD_DOTENV:
  from dotenv import load_dotenv
  load_dotenv()

BASE_PATH = os.environ['BASE_PATH']
TOKEN = os.environ['TOKEN']
BLOBS_CONN_STR = os.environ['BLOBS_CONN_STR']

TFS_HOST = os.environ['TFS_HOST']
TFS_PORT = int(os.environ['TFS_PORT'])
TFS_ENDPOINT = os.getenv('TFS_ENDPOINT') or '/v1/models/baseline:predict'

CORS = os.getenv('CORS', '*').split(',')

import os
from dslog import Logger

logger = Logger.click()
logger(f'Running DFY pipeline at "{BASE_PATH}"...')

import asyncio
from multiprocessing import Process
from fastapi import Request, Response
from fastapi.middleware.cors import CORSMiddleware
import tf.serving as tfs
from moveread.pipelines.dfy import DFYPipeline, queue_factory, Output, local_storage
from pipeteer import http
from kv.api import KV
from kv.fs import FilesystemKV
import kv.rest

tfparams = tfs.Params(host=TFS_HOST, port=TFS_PORT, endpoint=TFS_ENDPOINT)
tfparams: tfs.Params = { k: v for k, v in tfparams.items() if v is not None } # type: ignore

pipe = DFYPipeline()
get_queue = queue_factory(os.path.join(BASE_PATH, 'queues.sqlite'))
Qout = get_queue(('output',), Output)
storage = local_storage(BASE_PATH)
blobs = KV.of(BLOBS_CONN_STR)
images_path = blobs.base_path if isinstance(blobs, FilesystemKV) else None
if images_path:
  os.makedirs(images_path, exist_ok=True)
params = DFYPipeline.Params(logger=logger, token=TOKEN, tfserving=tfparams, blobs=blobs, images_path=images_path, **storage)
Qs = pipe.connect(Qout, get_queue, params)

artifs = pipe.run(Qs, params)

api = artifs.api
api.mount('/queues', http.mount(pipe, Qout, get_queue, params))
api.mount('/blobs', kv.rest.api(blobs))
api.add_middleware(CORSMiddleware, allow_origins=CORS, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@api.middleware('http')
async def auth_middleware(request: Request, call_next):
  images_path = request.url.path.startswith('/images/') and not '..' in request.url.path # could that hack work? let's just be safe
  if request.url.path == '/gamecorr/preds' or images_path or request.method == 'OPTIONS':
    return await call_next(request)
  
  auth = request.headers.get('Authorization')
  if not auth or len(parts := auth.split(' ')) != 2 or parts[0] != 'Bearer':
    logger(f'Bad authorization:', auth, level='DEBUG')
    return Response(status_code=401)
  if parts[1] != TOKEN:
    logger(f'Bad token: "{parts[1]}"', level='DEBUG')
    return Response(status_code=401)
  
  return await call_next(request)


def workers():
  ps = {
    id: Process(target=asyncio.run, args=(f,))
    for id, f in artifs.processes.items()
  }
  for id, p in ps.items():
    p.start()
    logger(f'Process "{id}" started at PID {p.pid}')
  for p in ps.values():
    p.join()

if __name__ == '__main__':
  workers()