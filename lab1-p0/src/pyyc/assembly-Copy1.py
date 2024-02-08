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

class Assembler(ast.NodeVisitor):
    
    def __init__(self):
        self.assembly = []
    
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
    

tree = ast.parse(expression)
assembly1 = Assembler()
assembly1.traverse(tree)
print(ast.dump(tree, indent = 4))
