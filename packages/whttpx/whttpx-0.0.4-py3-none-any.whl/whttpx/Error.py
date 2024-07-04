class Error_Auth(Exception):
  '''Credenciales de acceso'''
  def __init__(self, mensaje):
    self.mensaje = mensaje

  def __str__(self):
        return self.mensaje