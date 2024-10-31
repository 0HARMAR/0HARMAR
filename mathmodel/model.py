import pulp as pl
import numpy as np
import pandas as pd

# 参数初始化
num_land = 54
num_crops = 82
t = 1  # 将 t 固定为 1

# 创建模型
model = pl.LpProblem("Crop_Land_Optimization", pl.LpMaximize)

# 创建决策变量
x = pl.LpVariable.dicts(
    "x",
    (range(num_land), range(num_crops)),
    0,
    1,
    pl.LpContinuous
)

# 读取 Excel 数据并转换为 numpy 数组
Pjt = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='销售价格Pj').to_numpy()
Pjt = Pjt[0][1:]  # 删除第一列的元素
Pjt = Pjt.astype(float)  # 确保数据类型为 float

qjt = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='销售量qj').to_numpy()
qjt = qjt[0][1:]  # 删除第一列的元素
qjt = qjt.astype(float)  # 确保数据类型为 float

# 读取 Excel 文件中的数据
df = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='地块面积Si')

# 获取第三列数据（假设列索引从 0 开始）
Si = df.iloc[:, 2].to_numpy()
Si = Si.astype(float)

Dijt = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='亩产Dij').to_numpy()
Dijt = np.delete(Dijt, 0, axis=1)  # 删除第一列
Dijt = Dijt.astype(float)  # 确保数据类型为 float

Cijt = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='成本Cij').to_numpy()
Cijt = np.delete(Cijt, 0, axis=1)  # 删除第一列
Cijt = Cijt.astype(float)  # 确保数据类型为 float

# 目标函数
revenue = pl.lpSum(
    Pjt[j] * pl.lpSum(Si[i] * Dijt[i, j] * x[i][j] for i in range(27))
    for j in range(num_crops)
)

cost = pl.lpSum(
    Si[i] * Dijt[i, j] * x[i][j] * Cijt[i, j]
    for i in range(27)
    for j in range(num_crops)
)

# 目标函数 Z
z1 = revenue - cost
z2 = pl.lpSum(x[i][j] for i in range(num_land) for j in range(num_crops))
z3 = pl.lpSum(x[i][j] for i in range(num_land) for j in range(num_crops))

# 权重
w1 = 0.3
w2 = -0.3
w3 = 0.5

# 总目标函数
Z = w1 * z1 + w2 * z2 + w3 * z3

# 添加目标函数到模型
model += Z

# 添加约束条件
for i in range(num_land):
    for j in range(num_crops):
        model += x[i][j] >= 0  # 非负约束
        model += x[i][j] <= 1  # 变量值的上界约束

# 约束3：x[i][j] 和 x[i][j+41] 不能同时为 1
for i in range(num_land):
    for j in range(num_crops - 41):
        model += x[i][j] + x[i][j + 41] <= 1

# 约束4：特定作物的约束
for i in range(num_land):
    for j in [35, 36, 37]:
        model += x[i][j] == 0

# 约束5：指定条件的等式约束
for i in range(34):
    for j in [1, 2, 16]:
        model += x[i][j] == x[i][j + 41]

# 额外约束条件
for i in [0, 1, 25]:
    for j in [16, 17, 41] + list(range(57, 82)):
        model += x[i][j] == 0

# 添加约束条件：每块地里所有作物的占比之和为 1
for i in range(num_land):
    model += pl.lpSum(x[i][j] for j in range(num_crops)) == 1

# 求解模型
model.solve()

# 打印结果
print(f"目标函数值 Z: {pl.value(model.objective)}")

# 打印所有决策变量中值大于0的变量
for v in model.variables():
    print(f"{v.name} = {pl.value(v)}")
