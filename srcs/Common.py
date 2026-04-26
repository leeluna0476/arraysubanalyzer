from types import MappingProxyType
from ASTNode import ASTNode

class Common:
    _kind = 'Common'
    _registry = {}

    def __init__(self, idata=None):
        self._data = idata or {}
        self._id = self._data.get('id', -1)
        cls = type(self)
        if self._id != -1 and self._id not in cls._registry:
            cls._registry[self._id] = self

    def __repr__(self):
        return str(self._data)

    def __str__(self):
        return str(self._data)

    @property
    def id(self):
        return self._id

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
    def registry_view(cls):
        return MappingProxyType(cls._registry)

    @classmethod
    def get_obj(cls, cid):
        obj = cls._registry.get(cid)
        if not obj:
            obj = cls(ASTNode.get_node(cid))
        return obj

    @classmethod
    def _listup_data(cls, idata, l):
        if cls._kind == idata['kind']:
            l.append(idata)
        if 'inner' in idata:
            for d in idata['inner']:
                cls._listup_data(d, l)

    # listup the nodes of a specific kind (cls)
    @classmethod
    def listup_data(cls, cid=None):
        if cid:
            nodes = ASTNode.get_node(cid)
        else:
            nodes = ASTNode.raw_view()
        l = []
        cls._listup_data(nodes, l)
        return l

    # list up the cls objects from the whole ast data
    @classmethod
    def listup_obj(cls, cid=None):
        data_list = cls.listup_data(cid)
        return [cls.get_obj(data['id']) for data in data_list]

    # integrated cls obj list from a given parent list
    # -> extract cls objs from multiple objects (multiple dict data)
    @classmethod
    def listup_obj_under_parent(cls, parent_list):
        l = []
        for d in parent_list:
            l.extend(cls.listup_obj(d.id))
        return l
