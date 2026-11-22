from ..core import Entity, Vec2

class Actor(Entity) :

  LENGTH_UNIT: int = 100

  def __init__(self, position: Vec2) -> None:
    super().__init__()
    self.position: Vec2
    self.setPos(position)

  def _relativePos(self, position: Vec2) :
    if isinstance(self.parent, Actor) :
      return self.parent.position + (position * Actor.LENGTH_UNIT)
    return position * Actor.LENGTH_UNIT

  def setPos(self, position: Vec2) -> None :
    self.position = self._relativePos(position)

  def move(self, delta: Vec2) -> None :
    self.position += delta * Actor.LENGTH_UNIT
