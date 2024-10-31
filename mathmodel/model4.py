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
    Pjt[j] * pl.lpSum(Si[i] * Dijt[i, j] * x[i][j] for i in range(num_land-1))
    for j in range(num_crops)
)

cost = pl.lpSum(
    Si[i] * Dijt[i, j] * x[i][j] * Cijt[i, j]
    for i in range(num_land-1)
    for j in range(num_crops)
)

# 目标函数 Z
z1 = revenue - cost
z2 = pl.lpSum(x[i][j] for i in range(num_land) for j in range(num_crops))

# 权重
w1 = 0.3
w2 = 0.7

# 总目标函数
Z = w1 * z1 + w2 * z2

# 添加目标函数到模型
model += Z 


# 添加约束条件
for i in range(num_land):
    for j in range(num_crops):
        model += x[i][j] >= 0  # 非负约束
        model += x[i][j] <= 1  # 变量值的上界约束

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
    for j in [1, 2, 16]:
        model += x[i][j] == x[i][j + 41]

# 额外约束条件：某些作物不种植
for i in [0, 1, 25]:
    for j in [16, 17, 41] + list(range(57, 82)):
        model += x[i][j] == 0

# 添加约束条件：每块地里所有作物的占比之和为 1
for i in range(num_land):
    model += pl.lpSum(x[i][j] for j in range(num_crops)) == 1


for i in range(num_land):
    if i < 51 :
        model += x[i][40] == 0
        model += x[i][81] == 0

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

