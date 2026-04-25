import json
from Expr import ArraySubscriptExpr, ImplicitCastExpr, DeclRefExpr
from Decl import VarDecl
from asttools import filter_by_qualtype

with open('jsondump', mode='r', encoding='utf-8') as f:
    s = f.read()
    data = json.loads(s)

    ase_list = ArraySubscriptExpr.listup_obj(data)
    ice_list = ImplicitCastExpr.listup_from_parentlist(ase_list)
    dre_list = DeclRefExpr.listup_from_parentlist(ice_list)
    var_list = DeclRefExpr.listup_referenced_decl(dre_list)
    var_int_list = filter_by_qualtype(var_list, 'int')

    for v in var_int_list:
        print(v.name)
