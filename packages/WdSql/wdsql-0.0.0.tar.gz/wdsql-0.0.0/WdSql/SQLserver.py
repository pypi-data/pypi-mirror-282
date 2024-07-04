import traceback

import pyodbc

from wellog import loggen

from .Error import Error_Sql
from .Objects import Result

class SQLServer:
  def __init__(self):
    pass

  def select(self, key:str, query:str, params:list=None):
    status = True
    msg_error = ''

    data:dict = {}
    try:      
      conexion = pyodbc.connect(key)
      cursor = conexion.cursor()
      cursor.execute(query)
      columnas = [columna[0] for columna in cursor.description]
      data = cursor.fetchall()
      tabla = []
      for fila in data:
        fila_dict = {}
        for i in range(len(columnas)):
          fila_dict[columnas[i]] = fila[i]
        tabla.append(fila_dict)
      result = Result(data=tabla)
    except Exception as e:
      loggen.error(traceback.format_exc())
      status = False 
      msg_error = str(e)
    finally:
      cursor.close()
      conexion.close()
      if not status: raise Error_Sql(f'Error DB: {msg_error}', 501)
      return result