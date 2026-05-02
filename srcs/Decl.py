from Common import Common
from ASTNode import ASTNode

class Decl(Common):
    _kind = 'Decl'

class VarDecl(Decl):
    _kind = 'VarDecl'
    _registry = {}

    def __init__(self, idata=None):
        super().__init__(idata)
        self._initialized = 'init' in self._data
    
    # a c variable always has a name
    @property
    def name(self):
        return self._data['name']

    @property
    def initialized(self):
        return self._initialized

    def set_initialized(self, init):
        self._initialized = init
