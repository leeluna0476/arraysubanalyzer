import sys
import json
from Expr import ArraySubscriptExpr, ImplicitCastExpr, DeclRefExpr
from Decl import VarDecl
from Stmt import DeclStmt
from Operator import BinaryOperator
from ASTNode import ASTNode

integer_types = {'unsigned char', 'char', 'unsigned short', 'short',\
        'unsigned int', 'int', 'unsigned long', 'long',\
        'unsigned long long', 'long long'}

ASTNode.register_rawdata(json.loads(sys.stdin.read()))

declstmt_list = DeclStmt.listup_obj()
bo_list = [bo for bo in BinaryOperator.listup_obj() if bo.opcode == '=']
declstmt_bo = sorted(declstmt_list + bo_list, key=lambda x: x.line)
for x in declstmt_bo:
    if isinstance(x, DeclStmt):
        vardecl_list = VarDecl.listup_obj(x.id)
        for v in vardecl_list:
            dre_list = DeclRefExpr.listup_obj(v.id)
            if dre_list:
                v.set_initialized(True)
                for dre in dre_list:
                    if not dre.referenced_decl.initialized:
                        v.set_initialized(False)
                        break
            print(x.line, v.name, v.initialized)
    else:
        lvalue_list = DeclRefExpr.listup_obj(x.id, level=1)
        ice_list = [ice for ice in ImplicitCastExpr.listup_obj(x.id) if ice.qualtype in integer_types]
        rvalue_list = DeclRefExpr.listup_obj_under_parent(ice_list)
        init = True
        for rv in rvalue_list:
            if not rv.referenced_decl.initialized:
                init = False
                break
        for lv in lvalue_list:
            lv.referenced_decl.set_initialized(init)
            print(x.line, lv.referenced_decl.name, lv.referenced_decl.initialized)

## add more later
#
#bo_list = [x for x in BinaryOperator.listup_obj()\
#        if x.qualtype in integer_types\
#        and x.opcode == '=']
#
#ase_list = ArraySubscriptExpr.listup_obj()
#
#var_dict = {}
#for bo in bo_list:
#    dre_list = [x for x in DeclRefExpr.listup_obj(bo.id, level=1)\
#            if x.value_category == 'lvalue'\
#            if not x.referenced_decl.initialized]
#
#    for dre in dre_list:
#        vid = dre.referenced_decl.id
#        var_dict.setdefault(vid, []).append(bo)
#
#for ase in ase_list:
#    dre_list = [x for x in DeclRefExpr.listup_obj(ase.id)\
#            if x.value_category == 'lvalue'\
#            and x.qualtype in integer_types\
#            and not x.referenced_decl.initialized]
#
#    for dre in dre_list:
#        vid = dre.referenced_decl.id
#        var_dict.setdefault(vid, []).append(ase)
#
#with open('array_subscript_by_uninitialized_variable.csv', 'w', encoding='utf-8') as f:
#    f.write('line\n')
#    problematic_lines = []
#
#    for k, v in var_dict.items():
#        v.sort(key=lambda x: x.line)
#
#        vardecl = VarDecl.get_obj(k)
#        print('key:', vardecl.name)
#        for e in v:
#            print(e.id, type(e), e.line)
#
#        limit = len(v)
#        for i, n in enumerate(v):
#            if isinstance(n, BinaryOperator):
#                limit = i
#                break
#
#        problematic_lines.extend([v[j].line for j in range(limit)])
#
#    output = [f'{l}\n' for l in sorted(problematic_lines)]
#    f.writelines(output)
