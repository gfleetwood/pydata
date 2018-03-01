## pydata

A Python version of the tidyverse's most visibl feature of importing multiple libraries all at once. It was written and tested in Python 3.5, but I don't think there
would be issues in other versions. The usage is simple: 

```
from pydata import libs
globals().update(libs())
```

You now have access to numpy as np, scikit-learn as skl, pandas as pd, matplotlib.pyplot as plt, and plotnine as pn in the namespace. Installation of this package is only through this repo for now. Clone it and run `python setup.py install` to install the package on your system.
