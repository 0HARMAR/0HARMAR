class MyClass:
    class_variable = "shared by all instances"  # 类变量

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # 实例变量

# 创建多个实例
obj1 = MyClass("I am obj1")
obj2 = MyClass("I am obj2")

print(obj1.class_variable)  # 输出: shared by all instances
print(obj2.class_variable)  # 输出: shared by all instances

print(obj1.instance_variable) # output: I am obj1
print(obj2.instance_variable) # output: I am obj2

# 修改类变量
MyClass.class_variable = "modified class variable"

print(obj1.class_variable)  # 输出: modified class variable
print(obj2.class_variable)  # 输出: modified class variable

obj1.class_variable = "only obj1 modified"

print(obj1.class_variable)  # 输出: only obj1 modified
print(obj2.class_variable)  # 输出: modified class variable
