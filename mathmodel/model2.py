import numpy as np

x = np.zeros((54,41))

# x[i][j] j作物在地块i的占比

i = 0
j = 0

#constraints
#     |
#     v
x[i][j] >= 0 and x[i][j] <= 1 # Constraints 1

z1 = x[i][j] # 目标函数1

def trans(a):
    if a > 0:
        return 1
    elif a == 0:
        return 0

sum = None
const = 10
for i in range(1,55):
    sum += trans(x[i][const]) 

z2 = sum # 目标函数2

cost = [400,500,600] # 每种作物的种植成本

profit = [1000,2000,3000] # 每种作物的收益
# = 单价 × 亩产 × 亩数
# x[i][j] × i块地的亩数 × 亩产 × 单价

z3 = profit - cost # 目标函数3

w1 = 0.4
w2 = 0.3
w3 = 0.3

Z = z1 * w1 + z2 * w2 + z3 * w3 # 加权求和


# 不考虑多季，和一块地种多种作物