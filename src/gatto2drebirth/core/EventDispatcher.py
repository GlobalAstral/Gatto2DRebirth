from collections.abc import Callable
from .EventHandling import *
from .Vec2 import Vec2

class EventDispatcher :
  def __init__(self) -> None:
    self.__eventListeners__: dict[EventType | int, list[Callable[[Event], None]]] = {type: [] for type in EventType}
    self.__updateListeners__: list[Callable[[float], None]] = []
    self.__renderListeners__: list[Callable[[pygame.Surface, Vec2], None]] = []
    self.__setupListeners__: list[Callable[[], None]] = []

  def addEventListener(self, event: EventType | int, listener: Callable[[Event], None]) -> None :
    self.__eventListeners__[event].append(listener)
  def addUpdateListener(self, listener: Callable[[float], None]) -> None :
    self.__updateListeners__.append(listener)
  def addRenderListener(self, listener: Callable[[pygame.Surface, Vec2], None]) -> None :
    self.__renderListeners__.append(listener)
  def addSetupListener(self, listener: Callable[[], None]) -> None :
    self.__setupListeners__.append(listener)

  def _runSetup(self) -> None :
    for listener in self.__setupListeners__ :
      print(f"Executing: {listener!r}")
      listener()

  def _runRender(self, surface: pygame.Surface,  size: Vec2) -> None :
    for listener in self.__renderListeners__ : listener(surface, size)

  def _runUpdate(self, dt: float) -> None :
    for listener in self.__updateListeners__ : listener(dt)

  def _runEvent(self, event: Event) -> None :
    for listener in self.__eventListeners__[event.type] : listener(event)

  def _update(self, dt: float) -> None :
    self._runUpdate(dt)

  def _render(self, surface: pygame.Surface, winSize: Vec2) -> None :
    self._runRender(surface, winSize)

  def _setup(self) -> None :
    self._runSetup()

  def __iadd__(self, other: EventDispatcher):
    self.__setupListeners__.extend(other.__setupListeners__)
    self.__renderListeners__.extend(other.__renderListeners__)
    self.__updateListeners__.extend(other.__updateListeners__)
    for event, listeners in other.__eventListeners__.items():
      self.__eventListeners__.setdefault(event, []).extend(listeners)
    return self
