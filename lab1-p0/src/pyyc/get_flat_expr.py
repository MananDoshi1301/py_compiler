import ast
from ast import *
from flatten import PostfixVisitor

class Flat_Expr:
    def __init__(self, file_dir):
        self.file_dir = file_dir
        self.string_code_lst = []
        self.flat_expr = []
        self.flat_var_order = []
        ...
        
    def get_string_code(self):                
        string = ""
        with open(f"{self.file_dir}", 'r') as file:
        # Open the file and read     
            for line in file:        
                line = line.strip()
                # Remove empty blank spaced strings
                if line != "":            
                    self.string_code_lst.append(line)
        # print(self.string_code_lst)
        print("Code Reading: Success\n")        
        
    def convert_to_flat(self):
        # Form a combined expression separated by \n
        expression = "\n".join(str(expr) for expr in self.string_code_lst)

        # Parse and flat the tree
        tree = ast.parse(expression)
        postfix_visitor = PostfixVisitor()
        postfix_visitor.traverse(tree)

        # Get the Flat Expr list, var occurence order
        self.flat_expr = postfix_visitor.get_flat_expr()
        self.flat_var_order = postfix_visitor.return_var_order()
        # print("Flat Expression:", self.flat_expr)
        print("Code Flattening: Success\n")
        return {"flat_list": self.flat_expr, "var_order": self.flat_var_order}