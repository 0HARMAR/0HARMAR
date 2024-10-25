class pysicalobject:
    def __init__(self,mess,g) -> None:
        self.mess = mess
        self.g = g
        self.friction_coefficient = 0.5
        self.position = (0,0,0)
        
    
    def get_gravity(self):
        return self.mess * self.g
    
    def move(self,external_force,direction):
        fn = self.get_gravity() * self.friction_coefficient # 物体对地面的正压力
        if (external_force <= fn):
            #position not change
            pass
        else:
            
    
hemingyang = pysicalobject(63,9.98)

print(hemingyang.get_gravity())