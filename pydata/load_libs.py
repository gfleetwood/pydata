import importlib

def libs():
  
  requirements = [['pd', 'pandas']]
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
  
  If you're in a Jupyter notebook run `%matplotlib inline` to add inline visualizations.
  '''
  )
  
  return imported_libs
  
  

#import sklearn as sk
#import numpy as np
#import pandas as pd
#import plotnine as pn
#import matplotlib.pyplot as plt
