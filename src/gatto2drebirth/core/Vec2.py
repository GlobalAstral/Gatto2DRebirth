
import struct
from collections.abc import Callable
from math import sqrt

type number = int | float

def handle_operation(this: Vec2, other: object, operation: Callable[[number, number], number]):
  if isinstance(other, int | float) :
    return Vec2(operation(this.x, other), operation(this.y, other))
  elif isinstance(other, Vec2) :
    return Vec2(operation(this.x, other.x), operation(this.y, other.y))
  return NotImplemented

class Vec2 :
  @staticmethod
  def handle_operation(this: Vec2, other: object, operation: Callable[[number, number], number]):
    if isinstance(other, int | float) :
      return Vec2(operation(this.x, other), operation(this.y, other))
    elif isinstance(other, Vec2) :
      return Vec2(operation(this.x, other.x), operation(this.y, other.y))
    return NotImplemented

  def __init__(self, x: number, y: number) -> None:
    self.x: number = x
    self.y: number = y

  def __repr__(self) -> str:
    return f'Vec2({self.x}, {self.y})'
  def __str__(self) -> str:
    return f'({self.x}, {self.y})'

  def __format__(self, format_spec: str) -> str:
    return format(str(self), format_spec)

  def __bytes__(self) -> bytes:
    return struct.pack("ff", self.x, self.y)

  def __round__(self, ndigits: int | None = None):
    return Vec2(round(self.x, ndigits), round(self.y, ndigits))

  def __neg__(self):
    return Vec2(-self.x, -self.y)

  def __pos__(self):
    return Vec2(+self.x, +self.y)

  def __abs__(self):
    return Vec2(abs(self.x), abs(self.y))

  def __add__(self, other: object):
    return handle_operation(self, other, lambda x, y : x + y)

  def __sub__(self, other: object):
    return handle_operation(self, other, lambda x, y : x - y)

  def __mul__(self, other: object):
    return handle_operation(self, other, lambda x, y : x * y)

  def __truediv__(self, other: object):
    return handle_operation(self, other, lambda x, y : x / y)

  def __floordiv__(self, other: object):
    return handle_operation(self, other, lambda x, y : x // y)

  def __mod__(self, other: object):
    return handle_operation(self, other, lambda x, y : x % y)

  def __pow__(self, other: object):
    return handle_operation(self, other, lambda x, y: x**y)

  def __eq__(self, value: object) -> bool:
    if isinstance(value, Vec2) :
      return self.x == value.x and self.y == value.y
    if isinstance(value, tuple) :
      try :
        return self.x == value[0] and self.y == value[1] # type: ignore
      except Exception :
        return NotImplemented
    return NotImplemented

  def __hash__(self) -> int:
    return hash((self.x, self.y))

  def dot(self, other: Vec2) -> number :
    return self.x * other.x + self.y * other.y

  def cross(self, other: Vec2) -> number :
    return self.x * other.y - other.x * self.y

  def as_tuple(self) -> tuple[number, number] :
    return (self.x, self.y)

  def mag(self) -> number :
    return sqrt(self.x * self.x + self.y * self.y)

  def norm(self) -> Vec2 :
    m = self.mag()
    return Vec2(self.x / m, self.y / m)
