class Memory(Exception):
    
    _memory = None
    
    def __init__(self, size) -> None:
        Memory.size = size
        if Memory._memory == None:
            Memory._memory = bytearray(size)
            
    def mwrite(self,addr,data):
        Memory._memory[addr] = data
        
    def mread(self,addr):
        return Memory._memory[addr]
    
    def infosize (self):
        print(self.size)
        return self.size