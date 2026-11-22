
class Color :
  def __init__(self, value: int | tuple[int, int, int, int] | tuple[int, int, int]) -> None:
    self.a: int = 255
    self.r: int
    self.g: int
    self.b: int

    if isinstance(value, int) :
      self.a = (value >> 24) & 0xFF
      self.r = (value >> 16) & 0xFF
      self.g = (value >> 8) & 0xFF
      self.b = value & 0xFF
      return

    self.r = value[0]
    self.g = value[1]
    self.b = value[2]
    if len(value) > 3 :
      self.a = value[3]

  def as_tuple(self) -> tuple[int, int, int, int] :
    return (self.r, self.g, self.b, self.a)
