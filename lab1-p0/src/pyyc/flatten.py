# Add shebang
import ast
from ast import *
from stack_defn import Stack
import random



def done():
    print('-' * 80)
        
class PostfixVisitor(ast.NodeVisitor):
    
    def __init__(self):
        self.stack = Stack()
        self.counter = 0
        self.variables = {}
        self.flatExpr = []
        self.ctx = None
        self.runtimeVar = []
        self.var_order = []
        self.var_counter = 0
        self.generated_numbers = set()
        
    def __del__(self):
        
        # print("\n\nCompiled Variables: ")
        
        # for key in self.variables:
        #     print(f"{key}: {self.variables[key]}")
            
        # print("\n\nRuntime Variables: ")
        # string = ", ".join(str(var) for var in self.runtimeVar)
        # print(string)                
        
        # print("\n\nFlat Expressions: ")
        for expr in self.flatExpr:
            # print(expr)
            return self.flatExpr
            
        # self.stack.iterate() 
        
    # ------------------------------------ CUSTOM FUNCTIONS -----------------------------------
    
    def generate_id(self):
      while True:
        unique_digits = random.sample(range(10), 4)
        number = int(''.join(map(str, unique_digits)))        
        if number not in self.generated_numbers:
            self.generated_numbers.add(number)            
            return number
    
    def process_constants(self):
        val_type = self.stack.pop()
        val = self.stack.pop()
        return val_type, val                  
      
    # GEtting new variable name
    def get_new_var_name(self):
        name = f"t_{self.generate_id()}_{self.counter}"

        self.counter += 1      
        return name
    
    # Storing variable order
    def store_var_order(self, var_name):
        self.var_order.append(var_name)
        
    # return variable order
    def return_var_order(self):
        return self.var_order
    
    # String constant variables to dicts
    def store_constant_var(self, var_name, value):
        self.variables[var_name] = value
        self.store_var_order(var_name)
    
    # Storing runtime variables to list
    def store_runtime_var(self, var_name):
        self.runtimeVar.append(var_name)
        self.store_var_order(var_name)        
    
    def get_flat_expr(self):
        return self.flatExpr
        
    # --------------------------------------------------------------------------
    def traverse(self, node):
        # Traverse left subtree first and the right 
        for child in ast.iter_child_nodes(node):            
            self.traverse(child)            
        self.visit(node)
        
        
    # --------------------------------------------------------------------------

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
        self.stack_loader(node)        
    
    # -----------------------------------------------------------------------
    
    def stack_loader(self, node):
        name_type = type(node).__name__
        # print(f"Visited {name_type}")                
        
        if name_type == "Name":
            if node.id and node.id == "eval":
              # Create new var_name
              new_var_name = self.get_new_var_name()                                          
              
              # Append to runtime variables list
              self.store_runtime_var(new_var_name)
              
              # Append to flat expression
              self.flatExpr.append(f"{new_var_name} = eval(input())")
              
              # Push the new variable and its type to stack 
              self.stack.push(new_var_name)                
              self.stack.push("Constant_Variable")                
              
            elif node.id and node.id == "input":
                ...  
            
            elif self.ctx == "Load" and self.ctx is not None and self.stack.top() != "print":                                
                self.stack.push("Constant_Variable")                
        
        elif name_type == 'UnaryOp':
            # 2 operation down. Create new variable and push
            self.var_creator(name_type)
            
        
        elif name_type == 'BinOp':
            self.var_creator(name_type)            
        
        elif name_type == "Store":
            self.ctx = "Store"
            self.stack.push(name_type)
            
        elif name_type == "Load":
            self.ctx = "Load"
            # self.stack.push(name_type)
        
        elif name_type == 'Assign':
            # Always a variable assignment 
            self.var_creator(name_type)
            
        elif name_type == 'Call':                    
            self.var_creator(name_type)            
            
        elif name_type == 'Expr':
            self.var_creator(name_type)
        else:
            self.stack.push(name_type)
        # self.stack.iterate()
        
    # -----------------------------------------------------------------------         
        
    def var_creator(self, cmd):
                      
        if cmd == 'UnaryOp':
            
            # Can be constant or const_var
            val_type = self.stack.pop()
            new_var_name = None
            val = None
            expr = ""
            # Some constant
            if val_type == "Constant":
              val = self.stack.pop()    
              # First assign value to temp_var              
              temp_var = self.get_new_var_name()                        
              self.store_constant_var(temp_var, val)
              self.flatExpr.append(f"{temp_var} = {val}")
              
              # Secondy, assign new_var_name with negation of temp_var
              new_var_name = self.get_new_var_name()
              self.store_constant_var(new_var_name, -val)          
              expr = f"{new_var_name} = -{temp_var}"
              # Process on Usub
            
            # Variable has no previous operation of the eval input type
            elif val_type == "Constant_Variable":              
              var_name = self.stack.pop()
              
              if var_name not in self.runtimeVar:
                val = self.variables[var_name]                   
                
                new_var_name = self.get_new_var_name()
                self.store_constant_var(new_var_name, val)
                expr = f"{new_var_name} = -{var_name}"
              # Process on Usub              
            
              elif var_name in self.runtimeVar:                       
                new_var_name = self.get_new_var_name()
                self.store_runtime_var(new_var_name)
                expr = f"{new_var_name} = -{var_name}"
            
            if self.stack.pop() == "USub":
              self.stack.push(new_var_name)
              self.stack.push("Constant_Variable")
              
              self.flatExpr.append(expr)                                                      
                
                
        elif cmd == 'BinOp':
            lst_value = []
            eqn = []
            op = ""
            
            if self.stack.top() == "Constant":
                r_type, r_val = self.process_constants()                
                lst_value.append(r_val)
                eqn.append(r_val)
                
                op = self.stack.pop()
                
                if self.stack.top() == "Constant":      
                    l_type, l_val = self.process_constants()                       
                    lst_value.append(l_val)    
                    eqn.append(l_val)                   
                
                elif self.stack.top() == "Constant_Variable":
                    l_type, l_var_name = self.process_constants()
                    if l_var_name not in self.runtimeVar:
                        lst_value.append(self.variables[l_var_name])
                    eqn.append(l_var_name)
                
            elif self.stack.top() == "Constant_Variable":
                r_type, r_var_name = self.process_constants()
                if r_var_name not in self.runtimeVar:
                    lst_value.append(self.variables[r_var_name])
                eqn.append(r_var_name)
                # print("first |||", lst_value)
                
                op = self.stack.pop()
                
                if self.stack.top() == "Constant":      
                    l_type, l_val = self.process_constants()     
                    lst_value.append(l_val)    
                    eqn.append(l_val)                 
                
                elif self.stack.top() == "Constant_Variable":
                    l_type, l_var_name = self.process_constants()
                    # print("second |||", l_var_name)
                    if l_var_name not in self.runtimeVar:
                        lst_value.append(self.variables[l_var_name])
                    eqn.append(l_var_name)
                    
            if op == "Add":
                # For evaluating:                
                # New variable name:
                new_var_name = self.get_new_var_name()                
                
                # Append to dict of variables
                if len(lst_value) > 1:
                    self.store_constant_var(new_var_name, sum(lst_value))                    
                
                # Append variable to stack
                self.stack.push(new_var_name)
                self.stack.push("Constant_Variable")
                
                #Create a print stmt and append to flat
                string = f"{new_var_name} = {eqn[1]} + {eqn[0]}"                            
                if any(element in eqn for element in self.runtimeVar):
                    self.store_runtime_var(new_var_name)
                self.flatExpr.append(string)
              
            
        elif cmd == 'Call':
            # value_type = self.stack.pop()
            # value = self.stack.pop()
            # if value == "eval":
            #     self.stack.push("eval(input())")
            #     self.stack.push("Constant_Variable")
            ...
            
        elif cmd == 'Assign':
            
            val_type = self.stack.pop()
            val = self.stack.pop()
            var_name = self.stack.pop()
            if self.stack.pop() == 'Store':
                if val_type == "Constant_Variable" and val not in self.runtimeVar:
                    # self.stack.iterate()
                    temp = self.variables[val]
                    # print(temp, type(temp))
                    while not isinstance(temp, int):
                        temp = self.variables[temp]
                    self.store_constant_var(var_name, temp)                    
                elif val_type == "Constant_Variable" and val in self.runtimeVar:
                    self.store_runtime_var(var_name)
                    
                elif val_type == "Constant":                    
                    self.store_constant_var(var_name, val)
                
                # self.stack.push(var_name)
                # self.stack.push('Constant_Variable')
                # self.stack.iterate()
                
                self.flatExpr.append(f"{var_name} = {val}")
                # done()
                
        elif cmd == 'Expr':
            # self.stack.iterate()
                                    
            val_type = self.stack.pop()            
            val = self.stack.pop()
            if val_type == "Constant":
                # Get a variable name
                new_var_name = self.get_new_var_name()
                
                # Push variable value to dictionary
                self.store_constant_var(new_var_name, val)
                
                # Push variable expression to flat_expr
                self.flatExpr.append(f"{new_var_name} = {val}")
                # Push var name and type to stack                
                self.stack.push(new_var_name)
                self.stack.push(new_var_name)
                # Call this function again
                self.var_creator("Expr")
            
            if self.stack.is_empty() is False and self.stack.pop() == "print":
                self.flatExpr.append(f"print({val})")
                                                                                                                
            # done()

# print(ast.dump(tree, indent = 4))
# postfix_visitor = PostfixVisitor()
# postfix_visitor.traverse(tree)