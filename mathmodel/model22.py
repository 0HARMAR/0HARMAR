import numpy as np
from pulp import LpMaximize, LpProblem, LpVariable, lpSum
import pandas as pd

# 读取农作物信息（面积、作物类型、单价、产量等）
land_data = pd.read_excel('/home/ubuntu/下载/ABC.xlsx',sheet_name='销售价格')

cost = land_data.iloc[1].values.tolist()

cost = [float(value) for value in cost]

# 定义线性规划问题
problem = LpProblem("Crop_Optimization", LpMaximize)

# 地块数量和作物数量
num_plots = 26
num_crops = 15

# 定义变量 x[i][j]，代表第 i 块地上第 j 种作物的占比，0 <= x[i][j] <= 1
x = np.array([[LpVariable(f"x_{i}_{j}", lowBound=0, upBound=1) for j in range(num_crops)] for i in range(num_plots)])

profit = [1000, 2000, 3000]  # 每种作物的收益

# 目标函数1：z1，假设是所有地块和作物的加权和
z1 = lpSum([x[i][j] for i in range(num_plots) for j in range(num_crops)])

# 目标函数2：z2，最小化种植作物的数量
y = [LpVariable(f"y_{i}", cat='Binary') for i in range(num_plots)]
const = 2  # 假设关注的是第 2 列作物
for i in range(num_plots):
    problem += y[i] >= x[i][const] * 0.001  # 当 x[i][const] > 0 时，y[i] = 1
    problem += y[i] <= x[i][const] * 1000   # 当 x[i][const] == 0 时，y[i] = 0

z2 = lpSum(y)

# 目标函数3：z3，表示收益减去成本
z3 = lpSum([lpSum([x[i][j] * (profit[j] - cost[j]) for j in range(num_crops)]) for i in range(num_plots)])

# 添加约束条件：每块地的作物占比总和为 1，但允许多种作物同时存在
for i in range(num_plots):
    problem += lpSum([x[i][j] for j in range(num_crops)]) == 1

# 增加约束：每块地必须种植至少两种作物，即作物比例不能是完全的 0 或 1
for i in range(num_plots):
    for j in range(num_crops):
        problem += x[i][j] >= 0.3  # 强制每个地块至少有 10% 的比例分配给某种作物


# 权重
w1 = 0.4
w2 = -0.3  # 对 z2 施加负权重，使其最小化
w3 = 0.3

# 总的目标函数 Z
Z = w1 * z1 + w2 * z2 + w3 * z3
problem += Z

# 求解问题
problem.solve()

# 输出结果
for i in range(num_plots):
    for j in range(num_crops):
        print(f"x[{i}][{j}] = {x[i][j].varValue}")

# 输出目标函数值
print(f"Z = {Z.value()}")
