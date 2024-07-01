from typing_extensions import Sequence, TypeVar, TypedDict
import os
from pipeteer import QueueKV
from kv.sqlite import SQLiteKV
import moveread.pipelines.preprocess as pre
from moveread.pipelines.game_preprocess import StorageParams, Game

T = TypeVar('T')

def queue_factory(db_path: str):
  def get_queue(path: Sequence[str|int], type: type[T]) -> QueueKV[T]:
    return QueueKV.sqlite(type, db_path, '-'.join(str(p) for p in (path or ['Qin'])))
  return get_queue

class LocalStorage(TypedDict):
  games: SQLiteKV[Game]
  imgGameIds: SQLiteKV[str]
  buffer: SQLiteKV[dict[str, pre.Output]]

def local_storage(
  base_path: str, *,
  db_relpath: str = 'data.sqlite',
):
  """Scaffold local storage for the DFY pipeline."""
  os.makedirs(base_path, exist_ok=True)
  db_path = os.path.join(base_path, db_relpath)
  return LocalStorage(
    games=SQLiteKV.validated(Game, db_path, 'games'),
    imgGameIds=SQLiteKV[str].at(db_path, 'game-ids'),
    buffer=SQLiteKV.validated(dict[str, pre.Output], db_path, 'received-imgs'),
  )