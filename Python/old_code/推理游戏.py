import time
class person():
    name=None
    age=None
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
    def say(self,word):
        print(f"{self.name}:{word}")
    def kill(self):
        pass


A=person('A',24)
B=person('B',23)
C=person('C',18)
A.say('im not exist')
B.say('i tell the truth')
C.say('im exist')
print("B:hel……")
time.sleep((4))
print("you die")