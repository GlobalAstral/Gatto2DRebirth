from .Entity import Parent
from .Entity import Entity

class Scene(Parent) :
  def __init__(self, *args: Entity) -> None:
    super().__init__()
    super().__iadd__(args)
