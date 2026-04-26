from Common import Common
from Decl import VarDecl

class Expr(Common):
    _kind = 'Expr'

class ArraySubscriptExpr(Expr):
    _kind = 'ArraySubscriptExpr'
    _registry = {}

class ImplicitCastExpr(Expr):
    _kind = 'ImplicitCastExpr'
    _registry = {}

class DeclRefExpr(Expr):
    _kind = 'DeclRefExpr'
    _registry = {}

    def __init__(self, idata=None):
        super().__init__(idata)
        ref_decl_id = self._data['referencedDecl']['id']
        self._referenced_decl = VarDecl.get_obj(self._data['referencedDecl']['id'])

    @property
    def referenced_decl(self):
        return self._referenced_decl

    @classmethod
    def listup_referenced_decl(cls, dre_list):
        return [dre.referenced_decl for dre in dre_list]
