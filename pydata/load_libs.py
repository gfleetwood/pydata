def load_libs():
    
    import importlib
    
    try:
        requirements = pd.read_csv("~/.pydata/pydata.csv").values.tolist()
        msg = "\nLoading user defined libraries"
        print(msg)
    except:
        requirements = [['numpy', 'np'], ['pandas', 'pd'], ['matplotlib.pyplot', "plt"], 
                        ['sklearn.linear_model', "sk_lm"]]
        msg = "\nLoading default libraries"
        print(msg)
    
    imported_libs = {lib[1]: importlib.import_module(lib[0]) for lib in requirements}  
    globals().update(imported_libs)
    
    print("_"*len(msg) + "\n")
    loaded_libs = list(map(lambda x: print(x[0] + " loaded as " + x[1] + "\n"), requirements))
    loaded_libs
        
    return None
