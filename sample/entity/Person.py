from .Entity import Entity
from enum import Enum

class Gender(Enum):
  MALE='MALE'
  FEMALE='FEMALE'

class Person(Entity):
  def __init__(self, **kw):
    for key in kw.keys():
      setattr(self,key,kw.get(key))