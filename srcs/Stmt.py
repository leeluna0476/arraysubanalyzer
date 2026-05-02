from Common import Common
from Expr import DeclRefExpr
from Decl import VarDecl

# DeclStmt 중에서 VarDecl 뽑아내기.
class Stmt(Common):
    _kind = 'Stmt'

class DeclStmt(Stmt):
    _kind = 'DeclStmt'
    _registry = {}
