import pulp as pl
import numpy as np

# 参数初始化
num_land = 3
num_crops = 3

# 参数设置
Si = [80, 75, 60]  # 第I块地的亩数
Pj = [3, 4, 5]    # 第J作物的销售价
Dij = np.array([
    [400, 300, 200],  # 第1块地的亩产
    [400, 300, 200],  # 第2块地的亩产
    [400, 300, 200]   # 第3块地的亩产
])
Cij = np.array([
    [400, 350, 400],  # 第1块地的成本
    [400, 350, 400],  # 第2块地的成本
    [400, 350, 400]   # 第3块地的成本
])
qj = [10000, 20000, 15000]  # 第J作物2023年的销量

# 创建模型
model = pl.LpProblem("Crop_Optimization", pl.LpMaximize)

# 创建决策变量
x = pl.LpVariable.dicts("x", (range(num_land), range(num_crops)), lowBound=0, upBound=1, cat='Continuous')

# 创建辅助变量
y = pl.LpVariable.dicts("y", range(num_crops), lowBound=0, cat='Continuous')

# 添加约束来计算最小值
for j in range(num_crops):
    model += y[j] <= qj[j]  # 辅助变量 y[j] 至少要小于等于销量
    model += y[j] >= pl.lpSum(Si[i] * Dij[i, j] * x[i][j] for i in range(num_land))  # 辅助变量 y[j] 应大于等于计算值

# 目标函数
revenue = pl.lpSum(Pj[j] * y[j] for j in range(num_crops))
cost = pl.lpSum(Si[i] * Dij[i, j] * x[i][j] * Cij[i, j] for i in range(num_land) for j in range(num_crops))

# 不使用 trans 函数，而是直接用线性表达式计算 z2
const = 0
z2 = pl.lpSum(x[i][const] for i in range(num_land))

# 总目标函数
model += revenue - cost - z2

# 约束条件

# 约束 2: 每块地的作物总占比
for i in range(num_land):
    model += pl.lpSum(x[i][j] for j in range(num_crops)) == 1

# 约束 3: 不允许两个变量同时为 1
for i in range(num_land):
    for j in range(num_crops // 2):
        model += x[i][j] + x[i][j + num_crops // 2] <= 1

# 约束 4: 某些作物占比为 0 (根据实际需要设置)
for i in range(num_land):
    for j in [0, 1]:  # 示例，这里你需要根据具体要求调整
        model += x[i][j] == 0

# 约束 5: 对于特定区域的占比要求
# 示例，实际情况可能需要调整
for i in range(num_land):
    for j in range(num_crops // 2):
        model += x[i][j] == x[i][j + num_crops // 2]

# 约束 6: 特定地块和作物的占比为 0 (根据实际需要设置)
for i in [0, 1]:  # 示例，这里你需要根据具体要求调整
    for j in range(num_crops):
        model += x[i][j] == 0

# 求解模型
model.solve()

# 输出结果
print(f"目标函数值: {pl.value(model.objective)}")
for i in range(num_land):
    for j in range(num_crops):
        if pl.value(x[i][j]) > 0:
            print(f"x[{i}][{j}] = {pl.value(x[i][j])}")
