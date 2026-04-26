from Common import Common
from Stmt import DeclStmt

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

    # create a VarDecl object with cid under DeclStmt
    # does not create the other objects unlike listup_obj
    @classmethod
    def get_by_id(cls, cid):
        obj = cls.get_obj(cid)
        if not obj:
            declstmt_objs = DeclStmt.registry_view().values()
            for o in declstmt_objs:
                l = cls.listup_data(o.data)
                for d in l:
                    if d['id'] == cid:
                        obj = cls(d)
                        break
                if obj:
                    break
        return obj
