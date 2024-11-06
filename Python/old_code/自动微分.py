import torch
import math
x = torch.arange(4.0)
x.requires_grad_(True)
x.requires_grad
y = 2 * torch.dot(x,x)
y.backward()
print(x.grad)#打印梯度
print(x.grad == 4 * x)#验证梯度计算是否正确
x.grad.zero_()#清除之前累积的梯度值
y = x.sum()
y.backward()#调用反向传播函数
print(x.grad)

x.grad.zero_()
y = x*x*x
y.sum().backward()
print(x.grad)
