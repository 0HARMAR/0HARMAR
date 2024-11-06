import copy
import numpy as np
a=' '
b=0
list_position=np.zeros((15,40)).tolist()    #判断该位置是否有棋子
list=[[a for i in range(0,40)]for j in range(0,15)]     #输出15*40的空格作为棋盘
def piece_position(x_coordinate,y_coordinate):
  for i in range(0,len(x_coordinate)):
      if(i==0):
       list[x_coordinate[i]][y_coordinate[i]]='b'
       list_position[x_coordinate[i]][y_coordinate[i]]=1
      if(i%2==0):
       list[x_coordinate[i]][y_coordinate[i]] = 'b'
       list_position[x_coordinate[i]][y_coordinate[i]]=1
      if(i%2!=0):
       list[x_coordinate[i]][y_coordinate[i]] = 'w'
       list_position[x_coordinate[i]][y_coordinate[i]]=1
  for row in list:
      for item in row:
          print(item,end='\t')
      print()
###以上打印棋盘与棋子位置



def opponent(x_coordinate, y_coordinate):
      list_line2 = []
      list_line = []
      list_line2 = copy.deepcopy(x_coordinate[0:len(x_coordinate):2])
      for i in range(1, 16):
          list_line.append(copy.deepcopy(list_line2.count(i)))  # 每行棋子个数添加到列表list_line
          list_line3 = copy.deepcopy(list_line)
      list_line.sort(reverse=True)  # 降序排列
      l = list_line3.index(list_line[0]) + 1 #找出棋子最多行的行数


      list_row = []
      list_row2 = []
      list_row2 = copy.deepcopy(y_coordinate[0:len(x_coordinate):2])
      for i in range(1, 41):
          list_row.append(copy.deepcopy(list_row2.count(i)))  # 每列棋子个数添加到列表list_row
          list_row3 = copy.deepcopy(list_row)
      list_row.sort(reverse=True)  # 降序排列
      r = list_row3.index(list_row[0])+1  # 找出棋子最多列的列数


      c=[]
      for i in range(0, len(x_coordinate)):#将x列表中等于l的值的下标存入列表c
           if (x_coordinate[i]==l):
            c.append(i)
      d=[]
      if(list_line[0]>=list_row[0]):
       for i in range(0,len(c)):
          d.append(y_coordinate[c[i]])#根据l在x列表中的位置得到该位置对于y列表的元素
          d.sort(reverse=True)#d列表内是列数
          f=d[0]#找出列数最大的列
       while list_position[l][f+1]==1:
              f=f+1
       return l,f+1


      c1 = []
      for i in range(0, len(y_coordinate)):
        if (y_coordinate[i] == r):
            c1.append(copy.deepcopy(i))
      d1=[]
      if(list_line[0]<list_row[0]):
       for i in range(0,len(c1)):
           d1.append(copy.deepcopy(x_coordinate[c1[i]]))
           d1.sort(reverse=True)
           f1 = d1[0]#找出行数最大的行
       while list_position[f1+1][r]==1:
               f1=f1+1
       return f1+1,r
###程序对弈



#以下是主体
x_coordinate=[]
y_coordinate=[]
for i in range(1,1000):
    line = int(input('行:'))#玩家输入
    row = int(input('列:'))
    x_coordinate.append(copy.deepcopy(line))
    y_coordinate.append(copy.deepcopy(row))
    opponent(x_coordinate, y_coordinate)#程序对弈
    x,y=opponent(x_coordinate, y_coordinate)#程序棋子位置
    x_coordinate.append(copy.deepcopy(x))
    y_coordinate.append(copy.deepcopy(y))
    piece_position(x_coordinate, y_coordinate)#打印棋盘