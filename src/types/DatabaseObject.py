import abc
import inspect

class DatabaseObject(abc.ABC):
  def toInsertString(self):
    attributes = inspect.getmembers(self.__class__, lambda a: not(inspect.isroutine(a)))
    classProperties = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
    
    return "INSERT INTO {0} ({1}) VALUES {2}".format(
      self.__class__,
      ', '.join([val[0] for val in classProperties]),
      ', '.join([val[1] for val in classProperties]),
    )