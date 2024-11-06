class Car:  #定义一个car类
    original_mile=5  # 定义一个类属性
    def __init__(self,color,weight,name):  #根据Car类创建实例时会自动运行init方法
        self.name=name
        self.color=color
        self.weight=weight
        Car.original_mile+=5    #使用类属性必须类名.类属性的方式
    def run(self,mile): #run方法接受一个实参值，并输出结果
        print(f"The {self.name} car runs {mile} miles,its weight is {self.weight}")


print(Car.original_mile,Car.name)    #未创建实例时类属性original_mile的值，输出5
car_A=Car('red','10t','BMW')    #创建实例
#car_A.run(10)   #调用类方法
print(Car.original_mile,Car.name)    #创建实例后类属性original_mile的值，输出10，创建实例后类属性被修改

class Ecar(Car):    #继承Car父类
    def __init__(self,color,weight,name):
        super().__init__(color,weight,name)   #初始化父类属性

