class Common:
    _kind = 'Common'

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
    def data(self):
        return self._data

    @property
    def inner(self):
        return self._data.get('inner', [])

    @property
    def qualtype(self):
        return self._data.get('type', {}).get('qualType')

    @classmethod
    def get_obj(cls, cid):
        return cls._registry.get(cid)

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
        return [cls.get_obj(data['id']) or cls(data) for data in data_list]

    # integrated cls obj list from a given parent list
    # -> extract cls objs from multiple objects (multiple dict data)
    @classmethod
    def listup_from_parentlist(cls, parent_list):
        l = []
        for d in parent_list:
            l += cls.listup_obj(d.data)
        return l
