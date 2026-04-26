from Common import Common

class Decl(Common):
    _kind = 'Decl'

    def __init__(self, idata=None):
        super().__init__(idata)

class VarDecl(Decl):
    _kind = 'VarDecl'
    _registry = {}

    def __init__(self, idata=None):
        super().__init__(idata)
        print('Var init')
        self._initialized = False
    
    # a c variable always has a name
    @property
    def name(self):
        return self._data['name']
