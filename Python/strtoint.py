a = "124"# pure num string
print(0.1 + 0.2 == 0.3)
b = int(a)# convert to int

print(b , type(b))# 124 <class 'int'>

print(b+1)# 125,really convert to int

a1 = "124a"# string with none num

print(type('hmy'))
# print(int(a1,type(int(a1))))# get a value eror

print(int('00000011',2))