import json

from .server import ENV

_PYVERT:dict=None

class pyvert_setting(ENV):
  def __init__(self):
    super().__init__()
    global _PYVERT
    if not _PYVERT:
      with open(super().PROJECTS_SETTINGS('PYVERT')) as key:
        _PYVERT = json.load(key)

  # DEFAULT
  @property
  def RELOAD_PYVERT(self)->None:
    global _PYVERT
    super().RELOAD_SERVER_SETTINGS
    with open(super().PROJECTS_SETTINGS('PYVERT')) as key:
      _PYVERT = json.load(key)
  @property
  def SETTING(self):
    global _PYVERT
    return _PYVERT
  
  # SERVICE
  @property
  def HOST(self)->str:
    '''Domain where the server will be built'''
    global _PYVERT
    return _PYVERT['WEB_SERVICE']['HOST']  
  @property
  def PORT(self)->int:
    '''Port where the server will be built'''
    global _PYVERT
    return _PYVERT['WEB_SERVICE']['PORT']
  
  # USERS
  @property
  def USERS(self)->dict:
    '''users for use of some endpoints'''
    global _PYVERT
    return _PYVERT['USERS']