from Common import Common
from Stmt import DeclStmt
from ASTNode import ASTNode

class Decl(Common):
    _kind = 'Decl'

class VarDecl(Decl):
    _kind = 'VarDecl'
    _registry = {}

    def __init__(self, idata=None):
        super().__init__(idata)
        if 'init' in self._data:
            self._initialized = True
        else:
            self._initialized = False
    
    # a c variable always has a name
    @property
    def name(self):
        return self._data['name']

    @property
    def initialized(self):
        return self._initialized
