class ASTNode:
    _node = {}
    
    @classmethod
    def convert_rawdata_to_nodes(cls, rawdata):
        cid = rawdata['id']
        cls._node[cid] = rawdata
        if 'inner' in rawdata:
            for d in rawdata['inner']:
                cls.convert_rawdata_to_nodes(d)

    @classmethod
    def get_node_by_id(cls, cid):
        return cls._node.get(cid)
