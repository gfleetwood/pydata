# The Tidyverse In Python

## Intro

A Python version of the tidyverse's most visible feature of importing multiple libraries all at once. It was written and tested in Python 3.5 on Linux, but I don't think there would be issues in other versions and systems.

## Installation

The package can be installed through pip:

`pip install pydato`

Or by cloning the repo and running `python setup.py install`.

## Usage

pydato has only one function and using it requires help from Python's globals.

```
from pydato import load_libs
globals().update(load_libs())
```

In this call without any supplied arguments pydato checks to see if the file `"~/.pydato/pydato.csv"` exists in your root directory. If it doesn't, then the function loads numpy as np, pandas as pd, matplotlib.pyplot as plt, and sklearn.linear_model as sk_lm. You can create this file with two columns - the column names don't matter but the order does - to load a custom set of packages. For example:

```
package, alias
pandas, pd
numpy, np
```

Alternatively you can make use of the function's parameters:

`load_libs(file_path = None, include_defaults = False, verbose = True)`

Supply a `file_path` for the function to check for a csv in the same format outlined above to load libraries from custom file paths. Setting `include_defaults` to True tells the function to use the specified file path and the defaults from `"~/.pydata/pydata.csv"`. Set `verbose` to False to prevent the printing of information regarding the loaded packages and their aliases. 


