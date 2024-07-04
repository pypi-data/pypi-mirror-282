from loguru import logger

class Logger:
  def __init__(self, path:str='./logs'):
    self._path = path
    self._LEVEL_INFO={
      "sink":f'{self._path}/info.log',
      "level":"INFO",
      "rotation":"500 MB",
      "mode":"a"
    }
    self._LEVEL_DEBUG={
      "sink":f'{self._path}/debug.log',
      "level":"DEBUG",
      "rotation":"500 MB",
      "mode":"a"
    }
    self._LEVEL_ERROR={
      "sink":f'{self._path}/error.log',
      "level":"ERROR",
      "rotation":"500 MB",
      "mode":"a"
    }

  def setPath(self, path):
    '''Edit the location of the place to save the logs'''
    self._path=path
    self._LEVEL_INFO['sink']=f'{self._path}/info.log'
    self._LEVEL_DEBUG['sink']=f'{self._path}/debug.log'
    self._LEVEL_ERROR['sink']=f'{self._path}/error.log'
  
  def info(self, msg:str):
    '''General registration'''
    logger.remove()
    logger.add(**self._LEVEL_INFO)
    logger.info(msg)

  def debug(self, msg:str):
    '''Project debugging'''
    logger.remove()
    logger.add(**self._LEVEL_DEBUG)
    logger.debug(msg)

  def error(self, msg:str):
    '''System errors'''
    logger.remove()
    logger.add(**self._LEVEL_ERROR)
    logger.error(msg)