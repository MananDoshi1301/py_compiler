import sys
from get_flat_expr import Flat_Expr
import ast
from ast import *
from assembly import Assembler
import os
# ./pyyc mytests/test1.py

class Compile_P0:
    # pass sys.argv[1] to get_flat_
    def __init__(self):
        
        self.final_assembly = ""
        
        # Get file name from pyyc cmd
        self.file_dir = sys.argv[1]
        # self.file_dir = f"./tests/{self.file_dir}"
        self.working_dir = os.getcwd()
        
        # self.file_dir = f"{self.working_dir}/tests/{self.file_dir}"
        self.raw_file_name = self.file_dir.split("/")[-1].split(".")[0]        
        print("File Dir", self.file_dir)
        print("File Name", self.raw_file_name)
        # print("\n",self.file_dir)        
        
        
        # Creating a object for getting flat expression
        flat_obj = Flat_Expr(self.file_dir)
        flat_obj.get_string_code()
        
        flat = flat_obj.convert_to_flat()
        self.flat_expr = flat['flat_list']
        self.var_order = flat['var_order']
        flattened_code = "\n".join(self.flat_expr)
        print("\n",flattened_code, "\n")
        
        
        self.flat_ast = ast.parse(flattened_code)        
        
        self.total_var = len(self.var_order)
        # print(ast.dump(self.flat_ast, indent=2))
        
        self.starter_template = f"""
.global main
main:
    pushl %ebp 
    movl %esp, %ebp 
    subl ${4 * self.total_var}, %esp 
    pushl %ebx 
    pushl %esi
    pushl %edi
        """
        self.ending_template = f"""
    popl %edi 
    popl %esi
    popl %ebx
    movl $0, %eax 
    movl %ebp, %esp
    popl %ebp
    ret
        """
        print("Getting Flat Code: Success\n")
       
    def create_assembly(self):
        assembler = Assembler(self.var_order, self.flat_ast)
        code = "    "+ "\n    ".join(assembler.get_assembly())
        self.final_assembly = self.starter_template + "\n" + code + "\n" + self.ending_template                
        # print(self.final_assembly)
    
    def generate_assembly_file(self):
        file_arr = self.file_dir.split("/")
        file_arr[-1] = f"{self.raw_file_name}.s"
        file_arr = "/".join(file_arr)
        # print(file_arr)
        
        # print(self.final_assembly)
        with open(file_arr, 'w') as file:
            file.write(self.final_assembly)
            print("Done saving!")
        
    
    
        
compilation = Compile_P0()
compilation.create_assembly()
compilation.generate_assembly_file()