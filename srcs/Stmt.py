from Common import Common

# DeclStmt 중에서 VarDecl 뽑아내기.
class Stmt(Common):
    _kind = 'Stmt'

class DeclStmt(Stmt):
    _kind = 'DeclStmt'
    _registry = {}
