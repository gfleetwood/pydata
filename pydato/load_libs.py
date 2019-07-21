def load_libs(file_path = None, include_defaults = False, verbose = True):
    
    import importlib
    
    defaults = [['numpy', 'np'], ['pandas', 'pd'], ['matplotlib.pyplot', "plt"], 
                ['sklearn.linear_model', "sk_lm"]]
    requirements = []
    
    if file_path is not None:
        requirements.extend(pd.read_csv(file_path).values.tolist())
        msg = "\nLoading user specified libraries from custom file"
        
        if include_defaults is True:
            try:
                requirements.extend(pd.read_csv("~/.pydato/pydato.csv").values.tolist())
                msg = "\nLoading user specified libraries from custom file and base"
            except:
                print("include_defaults is True but the file `~/.pydato/pydato.csv` doesn't exist")
        print(msg)
    else:    
        try:
            requirements.extend(pd.read_csv("~/.pydato/pydato.csv").values.tolist())
            msg = "\nLoading user specified libraries from base"
            print(msg)
        except:
            requirements.extend(defaults)
            msg = "\nLoading default libraries"
            print(msg)
    
    imported_libs = {lib[1]: importlib.import_module(lib[0]) for lib in requirements}  
    
    print("_"*len(msg) + "\n")
    
    if verbose is True:         
        loaded_libs = list(map(lambda x: print(x[0] + " loaded as " + x[1] + "\n"), requirements))
        loaded_libs
        
    return imported_libs
