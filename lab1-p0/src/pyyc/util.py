import ast
from ast import *

def _get_vars(node, variables):
    if isinstance(node, Module):
        [_get_vars(x, variables) for x in node.body]
        return variables
    elif isinstance(node, Assign):
        _get_vars(node.targets[0], variables)
        _get_vars(node.value, variables)
        return
    elif isinstance(node, Expr):
        _get_vars(node.value, variables)
    elif isinstance(node, Name):
        if node.id not in ("print", "eval", "input"):
            variables.append(node.id)
        return
    elif isinstance(node, BinOp):
        _get_vars(node.left, variables)
        _get_vars(node.right, variables)
        return
    elif isinstance(node, UnaryOp):
        _get_vars(node.operand, variables)
        return
    elif isinstance(node, Call):
        _get_vars(node.func, variables)
        [_get_vars(arg, variables) for arg in node.args]
    
def get_vars_tree(tree):
    variables = []
    _get_vars(tree, variables)
    return list(set(variables))
    