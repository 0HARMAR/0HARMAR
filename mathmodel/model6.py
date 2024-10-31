import pulp as pl
import numpy as np
import pandas as pd

# 参数初始化
num_land = 54
num_crops = 82
t = 1  # 将 t 固定为 1

# 创建模型
model = pl.LpProblem("Crop_Land_Optimization", pl.LpMaximize)

# 创建决策变量，允许 x[i][j] 在 0 到 1 之间
x = pl.LpVariable.dicts(
    "x",
    (range(num_land), range(num_crops)),
    0,
    1,
    pl.LpContinuous
)

# 创建辅助二进制变量 z[i][j]，指示作物是否被种植
z = pl.LpVariable.dicts(
    "z",
    (range(num_land), range(num_crops)),
    0,
    1,
    pl.LpBinary
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
    Pjt[j] * pl.lpSum(Si[i] * Dijt[i, j] * x[i][j] for i in range(1,num_land-1))
    for j in range(num_crops)
)

cost = pl.lpSum(
    Si[i] * Dijt[i, j] * x[i][j] * Cijt[i, j]
    for i in range(1,num_land-1)
    for j in range(num_crops)
)
    
# 目标函数 Z
z1 = revenue - cost
z2 = pl.lpSum(z[i][j] for i in range(num_land) for j in range(num_crops))
z3 = pl.lpSum(x[i][j] for i in range(num_land) for j in range(num_crops))

# 权重
w1 = 0.5
w2 = 0.5
w3 = -0.1

# 总目标函数
Z = w1 * z1 + w2 * z2 + w3 * z3

# 添加目标函数到模型
model += z3

# 关联 x[i][j] 和 z[i][j] 的约束：当 z[i][j] = 1 时，x[i][j] 才能大于 0 并且最多为 1
for i in range(num_land):
    for j in range(num_crops):
        model += x[i][j] <= z[i][j]  # 如果 z[i][j] = 0，则 x[i][j] 必须为 0
        model += x[i][j] >= 0  # 确保 x[i][j] 非负
        model += x[i][j] <= 1  # x[i][j] 的上限为 1

# 地块上作物种植占比之和为 1
for i in range(num_land):
    model += pl.lpSum(x[i][j] for j in range(num_crops)) == 1

# 约束：每块地只能种植有限种作物，避免种植多个作物占比之和超过 1
for i in range(num_land):
    model += pl.lpSum(z[i][j] for j in range(num_crops)) <= 1  # 每块地只能种一种作物

# 关联 x[i][j] 和 z[i][j] 的约束
for i in range(num_land):
    for j in range(num_crops):
        model += x[i][j] <= z[i][j]  # 仅当 z[i][j] = 1 时，x[i][j] 才能大于 0

# 添加约束条件
for i in range(num_land):
    for j in range(num_crops):
        model += x[i][j] >= 0  # 非负约束
        model += x[i][j] <= 1  # 变量值的上界约束

Qij = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='种植面积').to_numpy
Qij = np.delete(Dijt, 0, axis=1)

# 约束2
for i in range(num_land-1):
    for j in range(num_crops-1):
        model += Qij[i][j] * x[i][j] == 0

# 约束3：x[i][j] 和 x[i][j+41] 不完全种植
for i in range(num_land):
    for j in range(num_crops - 41):
        model += x[i][j] + x[i][j + 41] <= 1

# 约束4：某些特定作物不种植
for i in range(num_land):
    for j in [35, 36, 37]:
        model += x[i][j] == 0

# 约束5：其他作物的比例一致性约束
for i in range(34):
    for j in range(1,17):
        model += x[i][j] == x[i][j + 41]

# 额外约束条件：某些作物不种植
for i in range(1,26):
    for j in list(range(16,42)) + list(range(57, 82)):
        model += x[i][j] == 0

# 添加约束条件：每块地里所有作物的占比之和为 1
for i in range(num_land):
    model += pl.lpSum(x[i][j] for j in range(num_crops)) == 1

# 确保羊肚菌（作物编号 42）只能在地块 51 到 54 中种植
for i in range(num_land):
    if i <= 51 or i >= 54:
        model += x[i][40] == 0
        model += x[i][81] == 0

# 约束：在第1到26块地上不种植第16到41和57到82种作物
for i in range(1, 27):
    for j in range(15, 42):
        model += x[i][j] == 0  # 第16到41种作物不种植
    for j in range(56, 82):
        model += x[i][j] == 0  # 第57到82种作物不种植

# 约束：地块27到34不种植编号为1到15、35到56、58到75和79到82的作物
for i in range(27, 35):  # 地块27到34
    for j in list(range(1, 16)) + list(range(35, 57)) + list(range(58, 76)) + list(range(79, 82)):
        model += x[i][j] == 0

# 约束：地块51到54不种植编号为1到16、35到57、76到82的作物
for i in range(51, 54):  # 地块51到54
    for j in list(range(1, 17)) + list(range(35, 58)) + list(range(76, 82)):  # 作物编号1到16、35到57、76到82
        model += x[i][j] == 0

# 约束：地块35到50不种植编号为1到16和35到78的作物
for i in range(35, 51):  # 地块35到50
    for j in list(range(1, 17)) + list(range(35, 79)):  # 作物编号1到16和35到78
        model += x[i][j] == 0

# 求解模型
model.solve()

# 作物列表
crops = ['黄豆', '黑豆', '红豆', '绿豆', '爬豆', '小麦', '玉米', '谷子', '高粱', '黍子', 
         '荞麦', '南瓜', '红薯', '莜麦', '大麦', '水稻', '豇豆', '刀豆', '芸豆', '土豆', 
         '西红柿', '茄子', '菠菜', '青椒', '菜花', '包菜', '油麦菜', '小青菜', '黄瓜', '生菜', 
         '辣椒', '空心菜', '黄心菜', '芹菜', '大白菜', '白萝卜', '红萝卜', '榆黄菇', '香菇', 
         '白灵菇', '羊肚菌']

# 打印所有决策变量中值大于0的变量，并输出地块对应的作物类型
for v in model.variables():
    if pl.value(v) > 0:
        # 解析变量名，例如 x_0_1 中，i=0, j=1
        name_parts = v.name.split("_")
        land_idx = int(name_parts[1])  # 地块编号 i
        crop_idx = int(name_parts[2])  # 作物编号 j

        # 映射 crop_idx 到正确的作物名称（两个季节）
        if crop_idx < 41:
            season = "第一季"
            crop_name = crops[crop_idx]  # 第一个季节的作物
        else:
            season = "第二季"
            crop_name = crops[crop_idx - 41]  # 第二个季节的作物

        # 打印地块编号、作物名称及其占比
        print(f"地块 {land_idx+1} 种植作物: {crop_name} ({season})，占比: {pl.value(v)}")

# 创建一个空的 DataFrame 用于存储结果
result_df = pd.DataFrame(index=range(num_land), columns=crops)

# 将模型结果填入 DataFrame
for v in model.variables():
    if pl.value(v) > 0:
        name_parts = v.name.split("_")
        land_idx = int(name_parts[1])
        crop_idx = int(name_parts[2])

        # 映射 crop_idx 到正确的作物名称（两个季节）
        if crop_idx < 41:
            season = "第一季"
            crop_name = crops[crop_idx]  # 第一个季节的作物
        else:
            season = "第二季"
            crop_name = crops[crop_idx - 41]  # 第二个季节的作物

        # 将值填入 DataFrame
        result_df.at[land_idx, crop_name] = pl.value(v)

# 填充 NaN 值为 0
result_df = result_df.fillna(0)

# 保存到 Excel 文件
output_file = 'mathmodel/C题/附件3/result1_1.xlsx'
result_df.to_excel(output_file)

print(f"结果已保存到 {output_file}")
