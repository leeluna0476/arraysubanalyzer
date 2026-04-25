class Decl:
    _kind = 'Decl'

    def __init__(self, idata=None):
        self._data = idata or {}

    @property
    def qualtype(self):
        return self._data.get('type', {}).get('qualType')

class VarDecl(Decl):
    _kind = 'VarDecl'

    def __init__(self, idata=None):
        super().__init__(idata)
        self._initialized = False
    
    # a c variable always has a name
    @property
    def name(self):
        return self._data['name']
