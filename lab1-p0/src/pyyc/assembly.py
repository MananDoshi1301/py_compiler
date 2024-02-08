import ast
from ast import *
from stack_defn import Stack
import random

expression = """
x = 12
t_9021_0 = eval(input())
t_4953_1 = 2
t_4983_2 = -t_4953_1
print(t_4983_2)
"""

# t_287_3 = x + t_4983_2
# t_1675_4 = t_9021_0 + t_287_3
# t_6572_5 = -x
# t_6340_6 = t_1675_4 + t_6572_5
# t_1804_7 = -t_6340_6
# t_9140_8 = 2 + t_1804_7
# t_6034_9 = 3 + t_9140_8
# print(t_6034_9)

class Assembler():
    
    def __init__(self, var_order, flat_ast):
        self.var_order = var_order
        self.flat_ast = flat_ast
        # print(ast.dump(self.flat_ast, indent =  4))
        self.var_order_dict = {}
        self.assembly = []
        for i, v in enumerate(self.var_order):
            self.var_order_dict[v] = (i+1)*4
            # print(f"{v}: {self.var_order_dict[v]}")
    
#     def __del__(self):
        
    
    def _parse_module(self):
        module = self.flat_ast.body
        assembly = ""
        for st_node in module:
            
            #################################################### Assign
            if isinstance(st_node, Assign):
                tar = st_node.targets[0]
                val = st_node.value
                
                ############################ Variable = Constant Assignment
                if isinstance(val, Constant):
                    self.assembly.append(f'movl ${val.value}, -{self.var_order_dict[tar.id]}(%ebp)')
                    
                ############################ Variable = Variable Assignment
                if isinstance(val, Name):
                    # print("Move Value id:", val.id, self.var_order_dict[val.id], "to:", tar.id, self.var_order_dict[tar.id])
                    # print(f'movl -{self.var_order_dict[val.id]}(%ebp), %eax')
                    # print(f'movl %eax, -{self.var_order_dict[tar.id]}(%ebp)')
                    self.assembly.append(f'movl -{self.var_order_dict[val.id]}(%ebp), %eax')
                    self.assembly.append(f'movl %eax, -{self.var_order_dict[tar.id]}(%ebp)')
                
                ############################ UnaryOp
                elif isinstance(val, UnaryOp):
                    op = val.op
                    operand = val.operand
                    if isinstance(operand, Name):
                        self.assembly.append(f'movl -{self.var_order_dict[operand.id]}(%ebp), %ecx')
                        self.assembly.append('negl %ecx')
                        self.assembly.append(f'movl %ecx, -{self.var_order_dict[tar.id]}(%ebp)')
                        
                    elif isinstance(operand, Constant):
                        self.assembly.append(f'movl ${operand.value}, %ecx')
                        self.assembly.append('negl %ecx')
                        self.assembly.append(f'movl %ecx, -{self.var_order_dict[tar.id]}(%ebp)')
                        
                        
                ############################ BinOP
                elif isinstance(val, BinOp):
                    left = val.left
                    right = val.right
                    # var + var 
                    if isinstance(left, Name) and isinstance(right, Name):
                        # print(f"{left.id} {right.id}")
                        self.assembly.append(f'movl -{self.var_order_dict[left.id]}(%ebp), %ecx')
                        self.assembly.append(f'movl -{self.var_order_dict[right.id]}(%ebp), %eax')
                        self.assembly.append(f'addl %ecx, %eax')
                        self.assembly.append(f'movl %eax, -{self.var_order_dict[tar.id]}(%ebp)')
                        
                    #const + var
                    elif isinstance(left, Constant) and isinstance(right, Name):
                        self.assembly.append(f'movl ${left.value}, %ecx')
                        self.assembly.append(f'movl -{self.var_order_dict[right.id]}(%ebp), %eax')
                        self.assembly.append(f'addl %ecx, %eax')
                        self.assembly.append(f'movl %eax, -{self.var_order_dict[tar.id]}(%ebp)')
                        
                        
                    # var + const
                    elif isinstance(left, Name) and isinstance(right, Constant):
                        # print("Var + const: ", left.id, right.value, tar.id)
                        self.assembly.append(f'movl -{self.var_order_dict[left.id]}(%ebp), %ecx')
                        self.assembly.append(f'movl ${right.value}, %eax')
                        self.assembly.append(f'addl %ecx, %eax')
                        self.assembly.append(f'movl %eax, -{self.var_order_dict[tar.id]}(%ebp)')
                        
                        
                    # const + const
                    elif isinstance(left, Constant) and isinstance(right, Constant):
                        self.assembly.append(f'movl ${left.value}, %ecx')
                        self.assembly.append(f'movl ${right.value}, %eax')
                        self.assembly.append(f'addl %ecx, %eax')
                        self.assembly.append(f'movl %eax, -{self.var_order_dict[tar.id]}(%ebp)')
                        
                ############################ Call
                elif isinstance(val, Call): # assume that this is eval(input()), this is only true for P0
                    self.assembly.append('call eval_input_int')
                    self.assembly.append(f'movl %eax, -{self.var_order_dict[tar.id]}(%ebp)')
            
            
            #################################################### Expr        
            elif isinstance(st_node, Expr):
                #assuming its a print statement:
                if isinstance(st_node.value, Call):
                    print_var = st_node.value.args[0]
                    self.assembly.append(f'movl -{self.var_order_dict[print_var.id]}(%ebp), %eax')
                    self.assembly.append(f'pushl %eax')                    
                    self.assembly.append('call print_int_nl')
                    self.assembly.append(f'addl $4, %esp')
               
    def get_assembly(self):
        self._parse_module()
        return self.assembly
                
''' 
    def traverse(self, node):
        # Traverse left subtree first and the right 
        for child in ast.iter_child_nodes(node):            
            self.traverse(child)            
        self.visit(node)
        
    def visit(self, node):  
        # Check if a node value push it to stack
        # print(f"\n{self.counter}: ")
        
        try:
            if (node.value == 0 or node.value) and type(node.value) is int:
                # print(f"Value: {node.value}")
                self.stack.push(node.value)                
        except:
            ...
            
        # Check if node id like 'print' and push to stack
        try:
            if node.id:
                avoid_list = ["eval", "input"]
                # print(f"Id: {node.id}")
                if node.id not in avoid_list:
                    self.stack.push(node.id)
        except:
            ...
        
        # It should be an object if not value or id 
        # check the type of operation                        
    
'''

if __name__ == "__main__":
    tree = ast.parse(expression)
    assembly1 = Assembler()
    assembly1._parse_module([], tree)
    print(ast.dump(tree, indent = 4))
