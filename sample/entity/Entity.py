class Entity(object):
  def __init__(self):
    pass
  def toDict(self):
    res = {}
    for key in dir(self):
      if not key.startswith('_'):
        attr = getattr(self,key,None)
        if not callable(attr):
          res[key]= attr
    return res