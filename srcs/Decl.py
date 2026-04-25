class Decl:
    _kind = 'Decl'
    _registry = {}

    def __init__(self, idata=None):
        self._data = idata or {}
        self._id = (idata and idata['id']) or -1
        # add meaningful objects to the registry
        if self._id != -1 and self._id not in Decl._registry:
            Decl._registry[self._id] = self

    @property
    def qualtype(self):
        return self._data.get('type', {}).get('qualType')

    @classmethod
    def exist(cls, vid):
        return vid in cls._registry

    @classmethod
    def existing_obj(cls, vid):
        return cls._registry.get(vid)

class VarDecl(Decl):
    _kind = 'VarDecl'

    def __init__(self, idata=None):
        super().__init__(idata)
        self._initialized = False
    
    # a c variable always has a name
    @property
    def name(self):
        return self._data['name']
