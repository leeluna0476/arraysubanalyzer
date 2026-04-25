from Decl import VarDecl

class Expr:
    _kind = 'Expr'

    def __init__(self, idata=None):
        self._data = idata or {}

    def __repr__(self):
        return str(self._data)

    def __str__(self):
        return str(self._data)

    @property
    def data(self):
        return self._data

    @property
    def inner(self):
        return self._data.get('inner', [])

    @property
    def qualtype(self):
        return self._data.get('type', {}).get('qualType')

    @classmethod
    def _listup_data(cls, idata, l):
        if idata['kind'] == cls._kind:
            l.append(idata)
        elif 'inner' in idata:
            for d in idata['inner']:
                cls._listup_data(d, l)

    # data -> cls data list
    # extract cls datas from a single dict data
    @classmethod
    def listup_data(cls, idata: dict):
        l = []
        if 'kind' in idata:
            cls._listup_data(idata, l)
        return l

    # data -> cls obj list
    # extract cls objs from a single dict data
    @classmethod
    def listup_obj(cls, idata: dict):
        data_list = cls.listup_data(idata)
        return [cls(data) for data in data_list]

    # integrated cls obj list from a given parent list
    # -> extract cls objs from multiple objects (multiple dict data)
    @classmethod
    def listup_from_parentlist(cls, parent_list):
        l = []
        for d in parent_list:
            l += cls.listup_obj(d.data)
        return l

class ArraySubscriptExpr(Expr):
    _kind = 'ArraySubscriptExpr'

class ImplicitCastExpr(Expr):
    _kind = 'ImplicitCastExpr'

class DeclRefExpr(Expr):
    _kind = 'DeclRefExpr'

    # 모든 reference에 대해 VarDecl 새로 생성하는 게 아니라...
    # VarDecl은 각 변수에 대해 하나씩만 존재하고
    # DeclRefExpr은 그걸 alias하는 방식으로 바꾸자.
    def __init__(self, idata=None):
        super().__init__(idata)
        ref_decl_id = self._data['referencedDecl']['id']
        if VarDecl.exist(ref_decl_id):
            self._referenced_decl = VarDecl.existing_obj(ref_decl_id)
        else:
            self._referenced_decl = VarDecl(self._data['referencedDecl'])

    @property
    def referenced_decl(self):
        return self._referenced_decl

    @classmethod
    def listup_referenced_decl(cls, dre_list):
        return [dre.referenced_decl for dre in dre_list]
