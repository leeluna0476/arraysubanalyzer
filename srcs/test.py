import json
from Expr import ArraySubscriptExpr, ImplicitCastExpr, DeclRefExpr
from Decl import VarDecl
from Stmt import DeclStmt
from asttools import filter_by_qualtype
from ASTNode import ASTNode

with open('jsondump', mode='r', encoding='utf-8') as f:
    s = f.read()
    data = json.loads(s)
    ASTNode.register_rawdata(data)

    ase_list = ArraySubscriptExpr.listup_obj()
    dre_list = DeclRefExpr.listup_obj_under_parent(ase_list)
    var_list = DeclRefExpr.listup_referenced_decl(dre_list)
    var_set = set(var_list)
    var_int_list = filter_by_qualtype(var_list, 'int')

    for v in var_set:
        print(f'id={id(v)}, name={v.name}, initialized={v.initialized}')
