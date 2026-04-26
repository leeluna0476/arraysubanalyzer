from Common import Common
from Stmt import DeclStmt

class Decl(Common):
    _kind = 'Decl'

    def __init__(self, idata=None):
        super().__init__(idata)

class VarDecl(Decl):
    _kind = 'VarDecl'
    _registry = {}

    def __init__(self, idata=None):
        super().__init__(idata)
        self._initialized = False
    
    # a c variable always has a name
    @property
    def name(self):
        return self._data['name']

    # create a VarDecl object with cid under DeclStmt
    # does not create the other objects unlike listup_obj
    @classmethod
    def get_id(cls, cid):
        obj = cls.get_obj(cid)
        if not obj:
            for v in DeclStmt._registry.values():
                l = cls.listup_data(v.data)
                for d in l:
                    if d['id'] == cid:
                        obj = cls(d)
                        break
                if obj:
                    break
        return obj
