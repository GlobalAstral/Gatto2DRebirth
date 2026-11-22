
from .Vec2 import Vec2
from .Entity import Parent
from enum import IntFlag, auto
import pygame

from .EventHandling import *

if __name__ != '__main__' :
  pygame.init()

class Window(Parent) :
  class Flags(IntFlag) :
    NONE = 0
    FULLSCREEN = auto()
    FULLSCREEN_DESKTOP = auto()
    OPENGL = auto()
    VULKAN = auto()
    HIDDEN = auto()
    BORDERLESS = auto()
    RESIZABLE = auto()
    MINIMIZED = auto()
    MAXIMIZED = auto()
    MOUSE_GRABBED = auto()
    KEYBOARD_GRABBED = auto()
    INPUT_FOCUS = auto()
    MOUSE_FOCUS = auto()
    ALLOW_HIGH_DPI = auto()
    MOUSE_CAPTURE = auto()
    ALWAYS_ON_TOP = auto()
    UTILITY = auto()

  @staticmethod
  def __deserialize_flags__(flags: Flags) -> dict[str, bool] :
    return { str(flag.name).lower(): bool(flags & flag) for flag in Window.Flags }

  def __init__(self, title: str, size: Vec2, flags: Flags) -> None:
    super().__init__()
    self.__win__: pygame.Window = pygame.Window(
      title,
      size.as_tuple(),
      pygame.WINDOWPOS_CENTERED,
      **Window.__deserialize_flags__(flags)
    )

    self.__surface__ = lambda : self.__win__.get_surface()
    self.__running__ = True
    self.__clock__ = pygame.time.Clock()

  def _render(self, surface: pygame.Surface, winSize: Vec2) -> None:
    surface.fill('black')
    super()._render(surface, winSize)
    self.__win__.flip()

  def mainloop(self, fps: float = 60) -> None :
    self._setup()

    while self.__running__ :
      for event in pygame.event.get() :
        if event.type == pygame.QUIT :
          self.__running__ = False
          continue

        try:
          ev_type = EventType(event.type)
        except ValueError:
          ev_type = event.type

        ev: Event = Event(ev_type, event)

        self._runEvent(ev)

      dt = self.__clock__.tick(fps) / 1000.0

      self._update(dt)

      self._render(self.__surface__(), Vec2(*self.__win__.size))

      
