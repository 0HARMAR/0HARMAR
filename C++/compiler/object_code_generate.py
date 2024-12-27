import json
from typing import List, Dict, Any,TextIO

path_prefix = r'C:\Just-For-Fun\C++\compiler\\'
registers_64bit = [
    "rax",  # Extended Accumulator
    "rbx",  # Extended Base
    "rcx",  # Extended Counter
    "rdx",  # Extended Data
    "rsi",  # Extended Source Index
    "rdi",  # Extended Destination Index
    "rbp",  # Extended Base Pointer
    "rsp",  # Extended Stack Pointer
    "r8",   # 64-bit General Purpose Register 8
    "r9",   # 64-bit General Purpose Register 9
    "r10",  # 64-bit General Purpose Register 10
    "r11",  # 64-bit General Purpose Register 11
    "r12",  # 64-bit General Purpose Register 12
    "r13",  # 64-bit General Purpose Register 13
    "r14",  # 64-bit General Purpose Register 14
    "r15"   # 64-bit General Purpose Register 15
]
var_list = []

def exit_code(asm : TextIO):
    asm.write('\tmovq $60, %rax\n')
    asm.write('\txor %rdi, %rdi\n')
    asm.write('\tsyscall\n')
    asm.write('\n')

def write_var(asm : TextIO,var_table : TextIO):
    var_table_data = json.load(var_table)
    for var in var_table_data["var"]:
        asm.write(f'{var["name"]}:      .quad {var["value"]}\n')
        var_ = variable(var["name"],var["scope"],var["type"],var["value"])
        var_list.append(var_)

class variable():
    def __init__(self,name,scope,type,value):
        self.name = name
        self.scope = scope
        self.type = type
        self.value = value
with (
    open(path_prefix+"var_table.json","r") as var_table,
    open(path_prefix+"go_used/syntax_tree.json","r") as syntax_tree,
    open(path_prefix+"add.S","w") as asm
):
    """
    1.first step
    according to var table
    set the var in asm
    """
    asm.write('.section .data\n')

    write_var(asm,var_table)

    asm.write('.section .text\n')
    asm.write('.global _start\n')
    asm.write('_start:\n') 
    
    """
    2.second step
    according to syntax tree
    calculate the exepress
    """
    
    # describe the reg and var binding relationship
    reg_binding_var : List[Dict[str,str]] = []
    # mov var to registers
    for var, reg in zip(var_list, registers_64bit):
        reg_var = {}
        reg_var[reg] = var.name
        reg_binding_var.append(reg_var)
        asm.write(f'\tmovq {var.name}(%rip), %{reg}\n')

    syntax_tree_data_ : List[Dict] = json.load(syntax_tree)
    for syntax_tree_data in syntax_tree_data_:
        sum = 0
        dest_var_index = None
        dest_var = ""
        if(syntax_tree_data["children"][0]["data"] != '*'): # syntax tree is two level
            dest_var = syntax_tree_data["data"]
            for index,var in enumerate(var_list):
                if var.name == dest_var:
                    dest_var_index = index
            for children in syntax_tree_data["children"]: # traverse the syntax tree
                for index,var in enumerate(var_list):
                    if var.name == children['data']:
                        sum += var.value
        dest_reg = ""
        for relation in reg_binding_var:
            if list(relation.values())[0] == dest_var:
                dest_reg = list(relation.keys())[0]
        asm.write(f'\taddq ${sum}, %{dest_reg}\n')

        # update the var table
        var_list[dest_var_index].value = sum
    # process exit code
    exit_code()
