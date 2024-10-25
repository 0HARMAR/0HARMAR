from memory import Memory
import json

path_prefix = r'Python/comsyssim/'

def decode_reg(reg1:str,reg2:str,regcode:dict):
    if (reg1 == "" and reg2 == ""):
        return int('00000000',2)
    elif (reg1 == "" and reg2 != ""):
        for key,value in regcode.items():
            if value == reg2: 
                return int('0000'+key,2)
    elif(reg1 and reg2):
        reg_1 = ""
        reg_2 = ""
        for key,value in regcode.items():
            if value == reg1:
                reg_1 = key
            elif (value == reg2):
                reg_2 = key
        return int(reg_1 + reg_2,2)
                
def fill_imvalue(imvalue:str,bin_ins:bytearray):
    if imvalue == "":
        for i in range(4):
            bin_ins.append(0)
    else:
        byte32_str = format(int(imvalue),'032b')
        byte_array = [int(byte32_str[i:i+8],2) for i in range(0,32,8)]
        for i in byte_array:
            bin_ins.append(i)

def write_to_memory(memory:Memory):
    with open (path_prefix+"test_code.s","r",encoding='utf-8') as testcode:
        with open(path_prefix+"regcode.json","r") as regcode:
            reg_code=json.load(regcode)
            print(memory.infosize())
            for line_num,line in enumerate(testcode,start=1):
                if line == "\n": # line is null 
                    continue
                elif line[:2] == "//": # line is a annotation
                    continue
                elif line[0] == ".": # line is a label
                    continue
                bin_ins:bytearray = []
                command = line.split()
                match command[0]: # command[0] : instruction
                    case 'mov':
                        bin_ins.append(0) # 0 is mov
                        if command[1].isdigit(): # command[1] : operand 1
                            bin_ins.append(decode_reg("",command[2],reg_code)) # register coding
                            fill_imvalue(command[1],bin_ins)
                        else:
                            bin_ins.append(decode_reg(command[1],command[2],reg_code))
                            fill_imvalue("",bin_ins)
                    case 'add':
                        bin_ins.append(1) # 1 is add
                        if command[1].isdigit():
                            bin_ins.append(decode_reg("",command[2],reg_code))
                            fill_imvalue(command[1],bin_ins)
                    case 'push':
                        bin_ins.append(3) # 3 is push
                        if command[1].isdigit():
                            pass
                        else:
                            bin_ins.append(decode_reg("",command[1],reg_code))
                            fill_imvalue("",bin_ins)
                    case 'call':
                        bin_ins.append(5) # 5 is call
                        if command[1].isdigit():
                            bin_ins.append(0) # no reg
                            fill_imvalue(command[1],bin_ins)
                    case 'ret':
                        bin_ins.append(6) # 6 is ret
                        bin_ins.append(decode_reg("","",reg_code))
                        fill_imvalue("",bin_ins)      
                    case 'jmp':
                        bin_ins.append(7) # 7 is jmp
                        bin_ins.append(decode_reg("","",reg_code))
                        fill_imvalue(command[1],bin_ins)
                    case 'itr':
                        bin_ins.append(8) # 8 is jmp
                        bin_ins.append(decode_reg("","",reg_code))
                        fill_imvalue(command[1],bin_ins)
                print(bin_ins)
                for i,byte in enumerate(bin_ins,start=0):
                    memory._memory[i + (line_num-1)*6] = byte
                                
        
                    
                        
memory1 = Memory(100)
write_to_memory(memory1)