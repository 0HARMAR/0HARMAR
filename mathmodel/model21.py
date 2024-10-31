import numpy as np
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# 创建线性规划问题，目标是最大化
problem = LpProblem("Maximization_Problem", LpMaximize)

# 定义变量 x[i][j]，并设置约束 0 <= x[i][j] <= 1
x = np.array([[LpVariable(f"x_{i}_{j}", lowBound=0, upBound=1) for j in range(41)] for i in range(54)])

# 定义目标函数1 z1
z1 = x[0][0]

# 定义新的二元变量 y[i]，表示 trans(x[i][const])
y = [LpVariable(f"y_{i}", cat='Binary') for i in range(1, 54)]

# 约束：如果 x[i][const] > 0 则 y[i] = 1，否则 y[i] = 0
const = 10
for i in range(1, 54):
    problem += y[i-1] <= x[i][const] * 1000  # 大于0的近似约束
    problem += y[i-1] >= x[i][const] * 0.001 # 小于0的近似约束

# 计算目标函数2 z2
z2 = lpSum(y)

# 加权求和的目标函数 Z
w1 = 0.4
w2 = 0.6
Z = z1 * w1 + z2 * w2

# 添加目标函数到问题中
problem += Z

# 求解该问题
problem.solve()

# 输出结果
for i in range(54):
    for j in range(41):
        print(f"x[{i}][{j}] = {x[i][j].varValue}")

# 输出最终的目标函数值
print(f"Z = {Z.value()}")
