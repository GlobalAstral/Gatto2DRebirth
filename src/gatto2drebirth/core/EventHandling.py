import pygame

from enum import IntEnum
from dataclasses import dataclass
from typing import ClassVar, Any

class EventType(IntEnum) :
  QUIT = pygame.QUIT
  USEREVENT = pygame.USEREVENT
  ACTIVEEVENT = pygame.ACTIVEEVENT
  KEYMAPCHANGED = pygame.KEYMAPCHANGED
  LOCALECHANGED = pygame.LOCALECHANGED
  CLIPBOARDUPDATE = pygame.CLIPBOARDUPDATE
  RENDER_TARGETS_RESET = pygame.RENDER_TARGETS_RESET
  RENDER_DEVICE_RESET = pygame.RENDER_DEVICE_RESET
  WINDOWSHOWN = pygame.WINDOWSHOWN
  WINDOWHIDDEN = pygame.WINDOWHIDDEN
  WINDOWEXPOSED = pygame.WINDOWEXPOSED
  WINDOWMOVED = pygame.WINDOWMOVED
  WINDOWRESIZED = pygame.WINDOWRESIZED
  WINDOWSIZECHANGED = pygame.WINDOWSIZECHANGED
  WINDOWMINIMIZED = pygame.WINDOWMINIMIZED
  WINDOWMAXIMIZED = pygame.WINDOWMAXIMIZED
  WINDOWRESTORED = pygame.WINDOWRESTORED
  WINDOWENTER = pygame.WINDOWENTER
  WINDOWLEAVE = pygame.WINDOWLEAVE
  WINDOWFOCUSGAINED = pygame.WINDOWFOCUSGAINED
  WINDOWFOCUSLOST = pygame.WINDOWFOCUSLOST
  WINDOWCLOSE = pygame.WINDOWCLOSE
  WINDOWTAKEFOCUS = pygame.WINDOWTAKEFOCUS
  WINDOWHITTEST = pygame.WINDOWHITTEST
  WINDOWICCPROFCHANGED = pygame.WINDOWICCPROFCHANGED
  WINDOWDISPLAYCHANGED = pygame.WINDOWDISPLAYCHANGED
  KEYDOWN = pygame.KEYDOWN
  KEYUP = pygame.KEYUP
  TEXTEDITING = pygame.TEXTEDITING
  TEXTINPUT = pygame.TEXTINPUT
  MOUSEMOTION = pygame.MOUSEMOTION
  MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN
  MOUSEBUTTONUP = pygame.MOUSEBUTTONUP
  MOUSEWHEEL = pygame.MOUSEWHEEL
  JOYAXISMOTION = pygame.JOYAXISMOTION
  JOYBALLMOTION = pygame.JOYBALLMOTION
  JOYHATMOTION = pygame.JOYHATMOTION
  JOYBUTTONDOWN = pygame.JOYBUTTONDOWN
  JOYBUTTONUP = pygame.JOYBUTTONUP
  JOYDEVICEADDED = pygame.JOYDEVICEADDED
  JOYDEVICEREMOVED = pygame.JOYDEVICEREMOVED
  CONTROLLERDEVICEADDED = pygame.CONTROLLERDEVICEADDED
  CONTROLLERDEVICEREMOVED = pygame.CONTROLLERDEVICEREMOVED
  CONTROLLERDEVICEREMAPPED = pygame.CONTROLLERDEVICEREMAPPED
  AUDIODEVICEADDED = pygame.AUDIODEVICEADDED
  AUDIODEVICEREMOVED = pygame.AUDIODEVICEREMOVED
  FINGERDOWN = pygame.FINGERDOWN
  FINGERUP = pygame.FINGERUP
  FINGERMOTION = pygame.FINGERMOTION
  MULTIGESTURE = pygame.MULTIGESTURE
  DROPBEGIN = pygame.DROPBEGIN
  DROPFILE = pygame.DROPFILE
  DROPTEXT = pygame.DROPTEXT
  DROPCOMPLETE = pygame.DROPCOMPLETE
  VIDEORESIZE = pygame.VIDEORESIZE
  VIDEOEXPOSE = pygame.VIDEOEXPOSE
  MIDIIN = pygame.MIDIIN
  MIDIOUT = pygame.MIDIOUT
  APP_TERMINATING = pygame.APP_TERMINATING
  APP_LOWMEMORY = pygame.APP_LOWMEMORY
  APP_WILLENTERBACKGROUND = pygame.APP_WILLENTERBACKGROUND
  APP_DIDENTERBACKGROUND = pygame.APP_DIDENTERBACKGROUND
  APP_WILLENTERFOREGROUND = pygame.APP_WILLENTERFOREGROUND
  APP_DIDENTERFOREGROUND = pygame.APP_DIDENTERFOREGROUND
  NOEVENT = pygame.NOEVENT
  NUMEVENTS = pygame.NUMEVENTS

@dataclass
class Event :
  CUSTOM_EVENTS: ClassVar[dict[str, int]] = { }

  type: EventType | int
  internal: pygame.Event

  @staticmethod
  def registerCustom(name: str) -> None :
    Event.CUSTOM_EVENTS[name] = pygame.event.custom_type()

  @staticmethod
  def fireCustom(name: str, **kwargs: Any) -> None :
    pygame.event.post(pygame.Event(Event.CUSTOM_EVENTS[name], **kwargs))

  @staticmethod
  def custom(name: str) -> int | None :
    try :
      return Event.CUSTOM_EVENTS[name]
    except KeyError :
      return None

  def __getitem__(self, key: str):
    return self.internal.dict[key]

  def __getattr__(self, name: str):
    try :
      return self.internal.dict[name]
    except KeyError :
      raise AttributeError(name) from None

  def __eq__(self, value: object) -> bool:
    if isinstance(value, EventType) :
      return self.type == value
    if isinstance(value, Event) :
      return self.type == value.type
    return NotImplemented
