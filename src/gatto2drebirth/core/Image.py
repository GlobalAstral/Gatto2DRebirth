
from PIL import Image
import pygame
from uuid import uuid5, NAMESPACE_DNS, UUID
from ..actors.Actor import Actor

from ..core.Vec2 import Vec2


class Texture :
  _loaded_textures: dict[UUID, Image.Image] = { }
  _namespace: UUID = uuid5(NAMESPACE_DNS, 'gatto2drebirth')

  def __init__(self, id: UUID) -> None:
    self._id = id

  @staticmethod
  def load(path: str) -> Texture :
    id = uuid5(Texture._namespace, path)
    if id in Texture._loaded_textures.keys() :
      return Texture(id)
    img = Image.open(path).convert('RGBA')
    Texture._loaded_textures[id] = img
    return Texture(id)

  @staticmethod
  def load_section(path: str, uv: Vec2, wh: Vec2) -> pygame.Surface :
    return Texture.load(path).section(uv, wh)
  
  @staticmethod
  def load_whole(path: str, wh: Vec2 = Vec2(0, 0)) -> pygame.Surface :
    return Texture.load(path).whole(wh)

  def section(self, uv: Vec2, swh: Vec2, wh : Vec2 = Vec2(0, 0) ) -> pygame.Surface :
    pos = uv * Actor.LENGTH_UNIT
    alt: Vec2 = pos + swh * Actor.LENGTH_UNIT # type: ignore
    img = Texture._loaded_textures[self._id].crop((pos.x, pos.y, alt.x, alt.y)) # type: ignore
    if wh != (0, 0) :
      img = img.resize((wh * Actor.LENGTH_UNIT).as_tuple(), Image.Resampling.NEAREST) # type: ignore
    return pygame.image.frombytes(img.tobytes(), img.size, 'RGBA')

  def whole(self, wh: Vec2 = Vec2(0, 0)) -> pygame.Surface :
    img = Texture._loaded_textures[self._id]
    if (wh != (0, 0)) :
      img = img.resize((wh * Actor.LENGTH_UNIT).as_tuple(), Image.Resampling.NEAREST) # type: ignore
    return pygame.image.frombytes(img.tobytes(), img.size, 'RGBA')
