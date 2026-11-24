from ..core.Image import Texture
from pathlib import Path
from os import mkdir
from enum import StrEnum

class ImageFormat(StrEnum):
  PNG = '.png'
  JPG = '.jpg'
  JPEG = '.jpeg'
  BMP = '.bmp'
  WEBP = '.webp'

  @staticmethod
  def contains(s: str) -> bool :
    try :
      ImageFormat(s)
      return True
    except ValueError :
      return False

class AssetsManager :
  _managers: dict[int, AssetsManager] = { }
  _count: int = 0

  @staticmethod
  def _id() -> int :
    temp = AssetsManager._count
    AssetsManager._count += 1
    return temp

  @staticmethod
  def retrieveImage(handle: int, path: str, extension: ImageFormat | None = None) -> Texture :
    manager = AssetsManager._managers[handle]
    folder = Path(f'{manager.namespace}/images/')
    if not folder.is_dir() :
      mkdir(folder)

    full_path = folder / f'{path.replace('.', '/')}'

    if extension is not None :
      full_path = full_path.with_suffix(f'{extension.value}')

    files: list[Path] = [
      file
      for file in full_path.parent.glob(f"{full_path.name}.*")
      if file.is_file() and ImageFormat.contains(file.suffix.lower())
    ]
    if len(files) == 0 :
      raise FileNotFoundError(f'Image {full_path} does not exist')

    if len(files) > 1 :
      raise FileExistsError(f'Image {full_path} is ambiguous')

    full_path = files[0]

    return Texture.load(f'{full_path}')
      
  def __new__(cls, namespace: str) -> int :
    instance = super().__new__(cls)
    id = AssetsManager._id()
    
    instance.__init__(namespace)
    AssetsManager._managers[id] = instance
    
    return id

  def __init__(self, namespace: str) -> None:
    self.namespace = namespace
