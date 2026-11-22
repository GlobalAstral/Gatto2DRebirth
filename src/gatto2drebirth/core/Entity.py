
from .Vec2 import Vec2
from .EventDispatcher import EventDispatcher
from typing import Self
import pygame

class Parent(EventDispatcher) :
  def __init__(self) -> None:
    super().__init__()
    self._children: list[Entity] = [] 

  def __iadd__(self, other: EventDispatcher | Entity | tuple[Entity, ...]) -> Self :
    if isinstance(other, Entity) :
      self._children.append(other)
      other.parent = self
      return self
    
    if isinstance(other, EventDispatcher) :
      return super().__iadd__(other)
    
    for node in other :
      self += node
    
    return self

  def __iter__(self):
    return iter(self._children)

  def __len__(self):
    return len(self._children)

  def __getitem__(self, key: int) -> Entity :
    return self._children[key]

  def __contains__(self, item: Entity):
    return item in self._children

  def __reversed__(self):
    return reversed(self._children)

  def _setup(self) -> None:
    super()._setup()
    for child in self : child._setup()

  def _render(self, surface: pygame.Surface, winSize: Vec2) -> None:
    super()._render(surface, winSize)
    for child in self : child._render(surface, winSize)

  def _update(self, dt: float) -> None:
    super()._update(dt)
    for child in self : child._update(dt)

class Entity(Parent) :
  def __init__(self, parent: Parent | None = None) -> None:
    super().__init__()
    self.parent: Parent | None = parent

