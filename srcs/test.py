import sys
import json
from Expr import ArraySubscriptExpr, ImplicitCastExpr, DeclRefExpr
from Decl import VarDecl
from Stmt import DeclStmt
from Operator import BinaryOperator
from ASTNode import ASTNode

ASTNode.register_rawdata(json.loads(sys.stdin.read()))

# add more later
integer_types = {'unsigned char', 'char', 'unsigned short', 'short',\
        'unsigned int', 'int', 'unsigned long', 'long',\
        'unsigned long long', 'long long'}

bo_list = filter(lambda x: x.qualtype in integer_types and x.opcode == '=',\
        BinaryOperator.listup_obj())

ase_list = ArraySubscriptExpr.listup_obj()

var_dict = {}
for bo in bo_list:
    dre_list = filter(lambda x: not x.referenced_decl.initialized,\
            filter(lambda x: x.value_category == 'lvalue',\
                      DeclRefExpr.listup_obj(bo.id, level=1)))
    for dre in dre_list:
        vid = dre.referenced_decl.id
        if vid in var_dict:
            var_dict[vid].append(bo)
        else:
            var_dict[vid] = [bo]

for ase in ase_list:
    dre_list = filter(lambda x: not x.referenced_decl.initialized,\
            filter(lambda x: x.qualtype in integer_types,\
            filter(lambda x: x.value_category == 'lvalue',\
                   DeclRefExpr.listup_obj(ase.id))))
    for dre in dre_list:
        vid = dre.referenced_decl.id
        if vid in var_dict:
            var_dict[vid].append(ase)
        else:
            var_dict[vid] = [ase]

with open('array_subscript_by_uninitialized_variable.csv', 'w', encoding='utf-8') as f:
    f.write('line\n')
    problematic_lines = []

    for k, v in var_dict.items():
        v.sort(key=lambda x: x.line)

        print('key:', ASTNode.get_node(k)['name'])
        for e in v:
            print(e.id, type(e), e.line)

        limit = len(v)
        for i in range(len(v)):
            if isinstance(v[i], BinaryOperator):
                limit = i
                break

        problematic_lines.extend([v[j].line for j in range(limit)])

    output = sorted([f'{l}\n' for l in problematic_lines])
    f.writelines(output)
