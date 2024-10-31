import numpy as np

#目标函数1
x= np.zeros((54,82))

# x[i][j] 是 作物j 在i块地的占比

Si = [80,75,60] # 第I块地的亩数

Pj = [3,4,5] # 第J作物的销售价

Dij = [400,300,200] # 第I块地J种作物的亩产

Cij = [400,350,400] # 第I块地J种作物的成本

qj = [10000,20000,15000] # 第J作物2023年的销量

revenue = sum(
    Pj[j] * min(
        qj[j],
        sum(Si[i] * Dij[i, j] * x[i, j] for i in range(3))
    )
    for j in range(3)
)

# 计算成本部分
cost = sum(
    Si[i] * Dij[i, j] * x[i, j] * Cij[i, j]
    for i in range(3)
    for j in range(3)
)

z1 = revenue - cost #目标函数1

def trans(a):
    if a > 0:
        return 1
    elif a == 0:
        return 0
    
const = 1

z2 = sum(trans(x[i][const]) for i in range(1,55)) # 目标函数2

Z = z1 - z2 #总目标函数 max z

x[i][j] <= 1 and x[i][j] >= 0 # 约束1

sum(x[i][j] for j in range(1,42)) == 1 and sum(x[i][j] for j in range(42,83)) == 1 #约束2

x[i][j] * x[i][j+41] == 0 # 约束3

x[i][j] == 0 if (j == 35 or j == 36 or j == 37) # 约束4

x[i][j] == x[i][j+41] (i == 1,2,...34,j == 1,2,16) # 约束5

x[i][j] == 0 (if i ==1,2,26 and (j == 16,17,41 or j == 57,58...82)

print(z1)


