class Error_Sql(Exception):
  '''Data Base'''
  def __init__(self, mensaje, code):
    self.mensaje = mensaje
    self._code = code

  def __str__(self):
        return self.mensaje
  
  @property
  def message(self):
     return self.mensaje
  
  @property
  def code(self):
     return self._code
