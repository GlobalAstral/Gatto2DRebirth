
from pygame import Surface

from gatto2drebirth.core.Vec2 import Vec2

from .Actor import Actor

class Sprite(Actor) :
  def __init__(self, position: Vec2, texture: Surface) -> None:
    super().__init__(position)
    self.texture = texture

  def _render(self, surface: Surface, winSize: Vec2) -> None:
    surface.blit(self.texture, self.position.as_tuple())
    return super()._render(surface, winSize)
