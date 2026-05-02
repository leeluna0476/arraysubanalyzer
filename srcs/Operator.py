from Common import Common
from Expr import DeclRefExpr

class Operator(Common):
    _kind = 'Operator'

class BinaryOperator(Operator):
    _kind = 'BinaryOperator'
    _registry = {}

    @property
    def opcode(self):
        return self._data.get('opcode')
