from gatto2drebirth.core.Color import Color
from gatto2drebirth.core.Vec2 import Vec2
from .Ellipse import Ellipse
from ..core.Vec2 import number

class Circle(Ellipse) :
  def __init__(self, position: Vec2, radius: number, color: Color, scale: Vec2 = Vec2(1, 1)) -> None:
    super().__init__(position, Vec2(radius, radius), color, scale)
