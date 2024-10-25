import json
import inspect
from memory import Memory
from write_ins_to_memory import write_to_memory

class Exception():
    extable = ["Invalid Instruction!","Invalid Regcode!"]
    def __init__(self) -> None:
        pass
    
    def exception(self,excpno):
        print(f"{self.__class__.__name__} : {Exception.extable[excpno]}",end=' ')
        print(f"in line {inspect.currentframe().f_back.f_lineno}")
        
class Register(Exception):
    def __init__(self, name) -> None:
        self.name = name
    value = 0  # init value is 0

class Cpu(Exception):
    def __init__(self,memory,pc) -> None:
        Cpu.ISA = ['mov', 'add', 'sub','call','ret','jmp','push','pop' ]
        Cpu.rsp = Register('rsp')
        Cpu.pc = Register('pc')
        Cpu.REG = [Cpu.rsp,Cpu.pc, ]
        for i in range(15):
            Cpu.REG.append(Register('r' + str(i + 1)))
        Cpu.Instruction = None
        Cpu.insdecoded = []
        Cpu.memory = memory
        Cpu.pc.value = pc
        

    def power_on(self):
        Cpu.rsp.value = Cpu.memory.infosize()-1
        while(True):
            self.fetch()
            self.decode()
            self.exec(Cpu.insdecoded[-3],Cpu.insdecoded[-2],Cpu.insdecoded[-1])
            print(f"instruction {Cpu.insdecoded[-3]} {Cpu.insdecoded[-2]} {Cpu.insdecoded[-1]} finished!")
            print("\033[31minfo registers:\033[0m")
            for i in range(15):
                print(f"{Cpu.REG[i].name} : {Cpu.REG[i].value}")

    def fetch(self):
        Cpu.Instruction = self.memory._memory[Cpu.pc.value:Cpu.pc.value+6] # fetch 6 bytes code
        Cpu.pc.value += 6
        
    
    def decode(self):
        byteins = Cpu.Instruction
        with open("Python/comsyssim/inscode.json",'r') as inscodefile:
            inscode = json.load(inscodefile)
            ins = ""
            for key,value in inscode.items(): # first byte ins type
                if int(key,2) == byteins[0]:
                    Cpu.insdecoded.append(value)
                    ins = value
            with open("Python/comsyssim/regcode.json",'r') as regcodefile: # second byte ins op reg
                reg_decoded = []
                regcode = json.load(regcodefile)
                regcodestr = format(byteins[1],'08b') # example 00000001
                if regcodestr[:4] == '0000': # decode first reg
                    reg_decoded.append("imvalue")
                elif regcodestr[:4] in regcode:
                    reg_decoded.append(regcode[regcodestr[:4]])
                else :
                    Exception.exception(self,1)
                if regcodestr[4:] == '0000': # decode second reg
                    Exception.exception(self,0)
                else:
                    reg_decoded.append(regcode[regcodestr[4:]])
                    
                match ins:
                    case 'mov':
                        if reg_decoded[0] == "imvalue": # decode first reg
                            # this is a im or addr
                            Cpu.insdecoded.append('imvalue')
                        elif reg_decoded[0] in regcode.values():
                            Cpu.insdecoded.append(reg_decoded[0])
                        else :
                            Exception.exception(self,1)

                        if reg_decoded[1] == '0000': # decode second reg
                            Exception.exception(self,0)
                        else:
                            Cpu.insdecoded.append(reg_decoded[1])

                        imvalue = 0 # decode rest 4 bytes
                        for i in range(4):
                            imvalue += byteins[2+i]

                        if(Cpu.insdecoded[-2] == "imvalue"):
                            Cpu.insdecoded[-2] = imvalue
                            
                    case 'add':
                        if reg_decoded[0] == "imvalue":
                            Cpu.insdecoded.append('imvalue')
                        elif reg_decoded[0] in regcode.values():
                            pass
                        if reg_decoded[1] in regcode.values():
                            Cpu.insdecoded.append(reg_decoded[1])
                        imvalue = 0 # decode rest 4 bytes
                        for i in range(4):
                            imvalue += byteins[2+i]
                        if(Cpu.insdecoded[-2] == "imvalue"):
                            Cpu.insdecoded[-2] = imvalue
                    case 'push':
                        Cpu.insdecoded.append(reg_decoded[1]) # push value or register
                        Cpu.insdecoded.append('NONE') # second oprand placeholder
                        
                    case 'call':
                        if byteins[1] == 0:
                            call_addr_int =  byteins[2]+byteins[3]+byteins[4]+byteins[5]
                            Cpu.insdecoded.append(call_addr_int)
                            Cpu.insdecoded.append('NONE') # second oprand placeholder
                    case 'ret':
                        Cpu.insdecoded.append('NONE') # first oprand placeholder
                        Cpu.insdecoded.append('NONE') # second oprand placeholder
                    case 'jmp':
                        if byteins[1] == 0:
                            jmp_addr_int = byteins[2]+byteins[3]+byteins[4]+byteins[5]
                            Cpu.insdecoded.append(jmp_addr_int)
                            Cpu.insdecoded.append('NONE')
                    

    gindex = lambda x: next((i for i, r in enumerate(Cpu.REG) if r.name == x), None) # given str reg name,return index of reg
    ismatch = lambda s: s.count('(') == s.count(')') and all(s[i] != '(' or s[i+1] != '(' for i in range(len(s) - 1)) # memory access\
    rmparen = lambda s: ''.join(c for c in s if c not in '()') # remove parentheses
    
    def exec(self, pc, op1=0, op2=0):
        if pc in Cpu.ISA:
            print(f"instruction: {pc}")
            match pc:
                case 'mov':
                    if isinstance(op2, str):  # dst is register
                        if op2[0] != '(':
                            if isinstance(op1,int):
                                index = Cpu.gindex(op2)
                                if index is not None:
                                    Cpu.REG[index].value = op1
                            else:
                                index_reg1 = Cpu.gindex(op1)
                                index_reg2 = Cpu.gindex(op2)
                                if index_reg1 and index_reg2 is not None:
                                    Cpu.REG[index_reg2].value = Cpu.REG[index_reg1].value
                        elif Cpu.ismatch(op2): # is a memory access
                            rmed = Cpu.rmparen(op2)
                            try:
                                intrmed = int(rmed)
                            except :
                                index = Cpu.gindex(rmed)
                                self.memory._memory[Cpu.REG[index].value] = op1
                            else:
                                self.memory._memory[intrmed] = op1
                    else:
                        Exception.exception(self,0)
                case 'add':
                    if isinstance(op1, str):
                        index1 = Cpu.gindex(op1)
                        index2 = Cpu.gindex(op2)
                        if index1 is not None and index2 is not None:
                            Cpu.REG[index2].value += Cpu.REG[index1].value
                    else:
                        if isinstance(op2, str):
                            index = Cpu.gindex(op2)
                            if index is not None:
                                Cpu.REG[index].value += op1
                                
                case 'push':
                    if op1.isdigit():
                        self.memory._memory[Cpu.rsp.value] = op1
                        self.rsp.value -= 1
                    else:
                        index = Cpu.gindex(op1)
                        self.memory._memory[Cpu.rsp.value] = Cpu.REG[index].value
                        self.rsp.value -= 1
                    
                case 'pop':
                    index = self.gindex(op1)
                    self.REG[index].value = self.memory._memory[self.rsp]
                    self.rsp.value += 1
                    
                case 'call':
                    if isinstance(op1,int):
                        # push return addr to stack
                        self.memory._memory[Cpu.rsp.value] = Cpu.pc.value
                        # set pc : target addr
                        self.pc.value = op1
                        self.rsp.value -= 1
                    
                case 'ret':
                    # set pc : stack top return addr
                    self.pc.value = self.memory._memory[Cpu.rsp.value+1]
                    # pop the return addr
                    self.rsp.value += 1
        else:
            Exception.exception(self,0)
        
    def inforeg(self, reg):
        index = Cpu.gindex(reg)
        if index is not None:
            print(f"{Cpu.REG[index].name} : {Cpu.REG[index].value}")



memory = Memory(100)
cpu0 = Cpu(memory,0)

write_to_memory(memory)

for i,byte in enumerate(memory._memory,start=0):
    print(f"byte{i} : {byte}")
    
cpu0.power_on()

cpu0.inforeg('r1')
cpu0.inforeg('r2')
cpu0.inforeg('r3')
