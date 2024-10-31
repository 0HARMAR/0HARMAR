from pulp import LpMaximize, LpProblem, LpVariable, lpSum


# 作物数据：价格 P_i，亩产量 Y_i，种植成本 C_i，预期销售量 D_i
P = [3, 5, 2]  # 各作物的销售价格
Y = [500, 300, 400]  # 各作物的亩产量
C = [100, 150, 120]  # 各作物的种植成本
D = [2000, 1500, 1800]  # 各作物的预期销售量

# 地块面积 A_j
A = [10, 12, 8]  # 每块地的面积

num_crops = len(P)
num_fields = len(A)
seasons = 2  # 两个季节

# 创建线性规划问题
problem = LpProblem("Maximize_Farming_Profit", LpMaximize)

# 创建决策变量 x_ij_s 表示作物 i 在地块 j 和季节 s 的种植面积
x = [[[LpVariable(f"x_{i}_{j}_{s}", lowBound=0) for s in range(seasons)] for j in range(num_fields)] for i in range(num_crops)]

# 辅助二进制变量 z_ij，表示是否同一块地在两季种植了同样的作物
z = [[LpVariable(f"z_{i}_{j}", cat="Binary") for j in range(num_fields)] for i in range(num_crops)]

# 目标函数：最大化种植收益
problem += lpSum(P[i] * Y[i] * x[i][j][s] - C[i] * x[i][j][s] for i in range(num_crops) for j in range(num_fields) for s in range(seasons))

# 约束条件 1：每块地每季的种植面积总和不能超过其面积
for j in range(num_fields):
    for s in range(seasons):
        problem += lpSum(x[i][j][s] for i in range(num_crops)) <= A[j]

# 约束条件 2：每种作物在两季的总产量不能超过预期销售量
for i in range(num_crops):
    problem += lpSum(Y[i] * x[i][j][s] for j in range(num_fields) for s in range(seasons)) <= D[i]

# 约束条件 3：重茬限制，第一季和第二季不能种植同样作物
M = 1000  # 一个大数，用于线性化约束

for i in range(num_crops):
    for j in range(num_fields):
        # 如果 z[i][j] = 1，则 x[i][j][0] 和 x[i][j][1] 至少一个为0
        problem += x[i][j][0] <= M * (1 - z[i][j])
        problem += x[i][j][1] <= M * (1 - z[i][j])

        # z[i][j] = 0 表示可以自由选择，但 x[i][j][0] 和 x[i][j][1] 不允许同时为非零
        problem += x[i][j][0] + x[i][j][1] <= M * z[i][j]

# 求解
problem.solve()

# 输出结果
for i in range(num_crops):
    for j in range(num_fields):
        for s in range(seasons):
            print(f"种植作物 {i+1} 在地块 {j+1} 的第 {s+1} 季面积: {x[i][j][s].varValue}")

# 输出最大收益
print(f"最大收益: {problem.objective.value()}")
