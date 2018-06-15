# The Tidyverse In Python

## Intro

A Python version of the tidyverse's most visible feature of importing multiple libraries all at once. It was written and tested in Python 3.5 on Linux, but I don't think there
would be issues in other versionsand systems. 

## Usage

Run these two lines of code and you're good to go.

```
from pydata import libs
globals().update(libs())
```

You now have access to numpy as np, scikit-learn.linear_model as skl_lm, pandas as pd, matplotlib.pyplot as plt, and plotnine as pn in the namespace. pandasql is also loaded, but you need to run `pdsql = lambda q: sqldf(q, globals())`  to reference it as `pdsql`.

Adding additional libraries is simple. Open `pydata/load_libs.py` and add your library to the requirements lists in the form `[<name_to_reference>, <name_of_package>]`. (For example, pandas in in the requirements as `['pd', 'pandas']`.)

## Installation

Installation of this package is only through this repo for now. Clone it and run `python setup.py install` to install the package on your system.
