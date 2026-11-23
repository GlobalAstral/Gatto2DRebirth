from ..core.Image import Texture
from pathlib import Path

class AssetsManager :
  _managers: dict[int, AssetsManager] = { }
  _count: int = 0

  _IMAGE_EXTENSIONS: set[str] = { '.png', '.jpg', '.jpeg', '.bmp', '.webp' }

  @staticmethod
  def _id() -> int :
    temp = AssetsManager._count
    AssetsManager._count += 1
    return temp

  @staticmethod
  def retrieveImage(handle: int, path: str) -> Texture :
    manager = AssetsManager._managers[handle]
    full_path = Path(f'{manager.namespace}/images/{path.replace('.', '/')}')

    files: list[Path] = [
      file
      for file in full_path.parent.glob(f"{full_path.name}.*")
      if file.is_file() and file.suffix.lower() in AssetsManager._IMAGE_EXTENSIONS
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
