from types import MappingProxyType

class ASTNode:
    _nodes = {}
    _raw = {}

    @classmethod
    def nodes_view(cls):
        return MappingProxyType(cls._nodes)

    @classmethod
    def raw_view(cls):
        return MappingProxyType(cls._raw)
    
    @classmethod
    def register_rawdata(cls, rawdata, pline=0):
        if not cls._raw:
            cls._raw = rawdata
        begin = rawdata.get('range', {}).get('begin', {})
        if begin:
            begin['line'] = max(begin.get('line', 0), pline)

        cid = rawdata['id']
        cls._nodes[cid] = rawdata
        if 'inner' in rawdata:
            for d in rawdata['inner']:
                cls.register_rawdata(d, begin.get('line', 0))

    @classmethod
    def get_node(cls, cid):
        return cls._nodes.get(cid, {})
