import pandas
import torch
import os
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from d2l import torch as d2l
from matplotlib_inline import backend_inline
'''os.makedirs(os.path.join('..', 'date'), exist_ok=True)#简单数据集
datefile = os.path.join('..', 'date', 'housetiny.csv')
with open(datefile, 'w') as f:
    f.write('NumRoom,Alley,Price\n')
    f.write('NA,Pave,127500\n')
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')
date = pandas.read_csv(datefile)
print(date)
x=torch.arange(4)
y=torch.arange(20).reshape(5,4)
m=torch.mv(y,x)#向量长度必须与矩阵列维数相同
print(m)'''
def f(x):#定义一个二次函数
    return 3*x**2-4*x
def numerical_lim(f,x,h):#计算导数
    return (f(x+h)-f(x))/h
h=0.1
'''for i in range(5):#f(x)在1处的导数
    print(f'h={h:.5f},numerical limit={numerical_lim(f,1,h):.5f}')
    h*=0.1'''

#导数可视化
def use_svg_display():#@save    #使用svg格式在Jupyter中显示绘图
    backend_inline.set_matplotlib_formats('svg')

def set_figsize(figsize=(3.5,2.5)): #@save      #设置matplotlib的图表大小
    use_svg_display()
    d2l.plt.rcParams['figure.figsize']=figsize
#@save
def set_axes(axes,xlabel,ylabel,xlim,ylim,xscale,yscale,legend):   #设置matplotlib的轴
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    axes.set_xscale(xscale)
    axes.set_yscale(yscale)
    if(legend):
        axes.legend(legend)
    axes.grid()
#@save
def plot(X,Y=None,xlabel=None,ylabel=None,legend=None,xlim=None,
         ylim=None,xscale='linear',yscale='linear',
         fmts=('-','m--','g-.','r:'),figsize=(3.5,2.5),axes=None):
    if legend is None:#绘制数据点
        legend=[]
    set_figsize(figsize)
    axes=axes if axes else d2l.plt.gca()

    def has_one_axis(X):    #如果x有一个轴，则输出True
        return (hasattr(X,"ndim") and X.ndim == 1 or isinstance(X,list)
            and not hasattr(X[0],"__len__"))

    if has_one_axis(X):
        X =[X]
    if Y is None:
        X,Y=[[]]*len(X),X
    elif has_one_axis(Y):
        Y = [Y]
    if len(X) != len(Y):
        X=X*len(Y)
    axes.cla()
    for x,y,fmt in zip(X,Y,fmts):
        if len(X):
            axes.plot(x,y,fmt)
        else:
            axes.plot(y,fmt)
    set_axes(axes,xlabel, ylabel, xlim, ylim, xscale, yscale, legend)
x=np.arange(0,3,0.1)
plot(x,[f(x),2*x-3],'x','f(x)',legend=['f(x)','Tangent line(x=1)'])
plt.show()
