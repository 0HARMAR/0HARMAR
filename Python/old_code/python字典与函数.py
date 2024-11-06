'''library={'kivy':'1','numpy':'2','pandas':'3','matplotlib':'4'}
for key in library.keys():#输出键key()方法
    print(key)
for values in library.values():#输出值values()方法
    print(values)
library['os']='1'#向字典添加键值对
print(library)'''

def printf(name,age,personality='kind',*Elses):#定义函数输出个人信息,一般将未知数量形参放到最后
    print(f"名字是:{name}\n年龄是:{age}\n其他:")
    for Eles in Elses:#遍历元组，输出其他信息
        print(Eles)
    print(f"most important :性格{personality}")
printf('hemingyang','18','active','love listening','love reading')#调用函数