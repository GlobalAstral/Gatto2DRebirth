from pygame import Surface

from gatto2drebirth.core.Vec2 import Vec2

from .Actor import Actor
from ..core.Color import Color

import pygame

class Rectangle(Actor) :
  def __init__(self, position: Vec2, size: Vec2, color: Color, scale: Vec2 = Vec2(1, 1)) -> None:
    super().__init__(position)

    self.size: Vec2 = size * Actor.LENGTH_UNIT
    self.color: Color = color
    self.scale: Vec2 = scale

    self._scaled = lambda : self.size * self.scale

  def _get_rect(self) -> pygame.Rect :
    scaled = self._scaled()
    return pygame.Rect(self.position.x, self.position.y, scaled.x, scaled.y)

  def _render(self, surface: Surface, winSize: Vec2) -> None:
    pygame.draw.rect(surface, self.color.as_tuple(), self._get_rect())
    return super()._render(surface, winSize)  
