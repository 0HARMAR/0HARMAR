import random
class person():
    name = None
    def guess(self, num,x,y):
        if(x==1):
         num=num/2
        if(y==1):
         num=num*2
         int(num)
        num = random.randint(0, num)
        print(num)
        return num
A=person()
B=person()
C=person()
b=random.randint(0,100)
x=0
y=0
for i in [1,2,3,4,5]:
   a = int(input('请输入:'))
   A.guess(a,x,y)
   B.guess(a,x,y)
   C.guess(a,x,y)
   x=0
   y=0
   if (a == b):
       print("WELL,YOU WIN")
       break
   elif(a>b):
        print("AM I THAT OLD???!!!")
        x=x+1
   else:
           print("VERY GOOD,BUT YOU WRONG")
           y=y+1
print(b)

