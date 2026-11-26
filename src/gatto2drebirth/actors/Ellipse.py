
import pygame

from gatto2drebirth.core.Vec2 import Vec2

from .Actor import Actor
from ..core.Color import Color
from typing import Callable

class Ellipse(Actor) :
  def __init__(self, position: Vec2, radius: Vec2, color: Color, scale: Vec2 = Vec2(1, 1)) -> None:
    super().__init__(position)

    self.radius: Vec2 = radius * Actor.LENGTH_UNIT
    self.color: Color = color
    self.scale: Vec2 = scale

    self._scaled: Callable[[], Vec2]  = lambda : (self.radius * 2) * self.scale # type: ignore

  def _get_rect(self) -> pygame.Rect :
    scaled = self._scaled()
    return pygame.Rect(self.position.x - scaled.x / 2, self.position.y - scaled.y / 2, scaled.x, scaled.y)

  def _render(self, surface: pygame.Surface, winSize: Vec2) -> None:
    pygame.draw.ellipse(surface, self.color.as_tuple(), self._get_rect())
    return super()._render(surface, winSize)  
