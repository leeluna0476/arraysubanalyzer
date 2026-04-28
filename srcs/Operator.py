from Common import Common

class Operator(Common):
    _kind = 'Operator'

class BinaryOperator(Operator):
    _kind = 'BinaryOperator'

    @property
    def opcode(self):
        return self._data.get('opcode')
