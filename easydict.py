class EasyDict():
    def __init__(self, initial_data={}):
        for key, val in initial_data.items():
            setattr(self, key, val)
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, val):
        if ' ' in key:
            normalize_key = key.replace(' ', '_') 
        setattr(self, key, val)
        setattr(self, normalize_key, val)
