import numpy as np
import pandas as pd
# 参数定义
w1 = 0  # 预期销售量变化率
w2 = 0  # 亩产量的变化率
w3 = 0  # 农作物成本的变化率
w4 = 0  # 销售价格的变化率

# 决策变量，第 t 年在第 i 块地种植 j 种作物的面积比例
Xijtk = np.zeros((54, 42, 7, 3))  # 54 块地，42 种作物，7 年，3 种植季

# 其他变量
Dijtk = None  # 亩产量
Pijtk = None  # 销售价格
qijtk = None  # 销售量
Si = None     # 地块面积
Cijtk = None  # 成本

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
# 目标函数 1
z1 = np.sum(
    Pijtk * (1 + w4) * np.minimum(
        qijtk * (1 + w1),
        np.sum(Si * (1 + w2) * Dijtk * Xijtk, axis=0)
    )
)

# 目标函数 2 - 最大化 Xijtk
z2 = np.max(Xijtk)

# 定义转换函数
def trans(a):
    if a > 0:
        return 1
    elif a == 0:
        return 0
    else:
        return -1  # 根据需要，可以调整

# 目标函数 3
z3 = np.sum(trans(Xijtk))

# 约束条件1 - 确保 Xijtk 在 0 到 1 之间
constraints = (Xijtk >= 0) & (Xijtk <= 1)

#约束条件2 - 对于特殊的豆类作物，要求每三年内至少种植一次豆类作物
for j in [1,2,3,4,5,17,18,19]:
    Xijtk[i][j][t][k] + Xijtk[i][j][t+1][k] + Xijtk[i][j][t+2][k] != 0

#约束条件3 - 每种单季作物在每个地块（含大棚）都不能连续重茬种植。
Xijtk[i][j][t][k] == Xijtk[i][j][t+1][k]

#约束条件4 - 每一块地都种满农作物。
sum(
    (Xijtk[i][j][t][k])
    for j in range(1,43)
) == 1

#约束条件5 - 每种两季作物在每个地块（含大棚）都不能连续重茬种植。
Xijtk[i][j][t][2] * Xijtk[i][j][t][3] == 0

#约束条件6 - 对于特殊的j=35,36,37，这三种作物为水浇地第二季作物。
for j in [35,36,37]:
    Xijtk[i][j][t][2] == 0

#约束条件7 - 对于特殊的j=16时，保证水稻在水浇地第一季和第二季的存在情况是一样的。
Xijtk[i][16][t][2] == Xijtk[i][16][t][3]

#约束条件8 - 只在平旱地、梯田、山坡地种植粮食类作物（水稻除外）。
sum(
    (sum(
        (Xijtk[i][j][t][1])
        for j in range(16,42)
    ))
    for i in range(1,27)
) == 0

#约束条件9 - 第一季只在水浇地、普通大棚、智慧大棚种植蔬菜（大白菜、白萝卜、红萝卜除外）和水浇地种植单季水稻。
sum(
    (sum(
        (Xijtk[i][j][t][2])
        for j in range(1,42)
    ))
    for i in range(1,27)
)+sum(
    (sum(
        (Xijtk[i][j][t][2])
        for j in range(1,16)
    )
    +
    sum(
        (Xijtk[i][j][t][2])
        for j in range(35,42)
    ))
    for i in range(27,35)
) == 0

# 约束条件10 -