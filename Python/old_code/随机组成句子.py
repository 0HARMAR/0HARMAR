import random
S={1:'i',2:'he',3:'she',4:'it',5:'you'}
V={1:'am',2:'is',3:'are'}
O={1:'kind',2:'good',3:'live',4:'lying'}
i=random.randint(1,5)
i1=random.randint(1,3)
i2=random.randint(1,4)
if (i==1):
    i1=1
if (i==2 or i==3 or i==4):
    i1=2
if (i==5):
    i1=3
print(S[i],V[i1],O[i2],i,i1,i2)