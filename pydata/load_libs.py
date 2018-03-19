import importlib

def libs():
  
  requirements = [
    ['pd', 'pandas'], ['skl', 'sklearn'], ['np', 'numpy'], ['pn', 'plotnine'], ['plt', 'matplotlib.pyplot'],
    ['lz', 'logzero'], ['pandasql', 'pandasql'],
    ]
  imported_libs = {lib[0]: importlib.import_module(lib[1]) for lib in requirements}
  print(
  ''' 
  pydata
  _______
  
  numpy loaded as np
  pandas loaded as pd
  scikit-learn loaded as sk
  matplotlib.pyplot loaded as plt
  plotnine loaded as pn
  
  
  pandasql is also loaded. For usage, please run `pdsql = lambda q: sqldf(q, globals())` and reference
  `pdsql`.
  '''
  )
  
  return imported_libs

