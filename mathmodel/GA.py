import numpy as np
import pandas as pd

# 参数定义
w1 = 0  # 预期销售量变化率
w2 = 0  # 亩产量的变化率
w3 = 0  # 农作物成本的变化率
w4 = 0  # 销售价格的变化率

# 决策变量，第 t 年在第 i 块地种植 j 种作物的面积比例
Xijtk_shape = (54, 42, 7, 3)  # 54 块地，42 种作物，7 年，3 种植季

# 读取 Excel 数据并转换为 numpy 数组
Pjt = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='销售价格Pj').to_numpy()
Pjt = Pjt[0][1:]  # 删除第一列的元素
Pjt = Pjt.astype(float)  # 确保数据类型为 float

qjt = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='销售量qj').to_numpy()
qjt = qjt[0][1:]  # 删除第一列的元素
qjt = qjt.astype(float)  # 确保数据类型为 float

df = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='地块面积Si')
Si = df.iloc[:, 2].to_numpy().astype(float)

Dijt = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='亩产Dij').to_numpy()
Dijt = np.delete(Dijt, 0, axis=1).astype(float)

Cijt = pd.read_excel('/home/ubuntu/下载/data.xlsx', sheet_name='成本Cij').to_numpy()
Cijt = np.delete(Cijt, 0, axis=1).astype(float)

# 定义目标函数z1
def z1(P, w, q, S, D, X, C):
    total_sum = 0
    
    for k in range(3):
        for t in range(len(P[k])):
            part1_sum = sum(S[i] * D[i][t] * (1 + w[2]) * X[i][t] for i in range(len(X)))
            total_sum += P[k][t] * (1 + w[3]) * min(q[k][t] * (1 + w[0]), part1_sum)

    part2_sum = sum(S[i] * D[i][t] * (1 + w[2]) * X[i][t] for i in range(len(X)))
    total_sum += part2_sum

    for t in range(len(q)):
        total_sum -= q[t] * (1 + w[0]) * 0.5 * P[t] * (1 + w[3])

    for k in range(3):
        for i in range(len(S)):
            total_sum -= S[i] * D[i][k] * (1 + w[2]) * X[i][k] * C[i][k] * (1 + w[2])

    return total_sum

# 目标函数和适应度函数
def fit_func(individual):
    Xijtk = individual.reshape(Xijtk_shape)
    w = [w1,w2,w3,w4]

    #目标函数1
    z1 = z1(Pjt,w,qjt,Si,Dijt,Xijtk,Cijt)
    
    # 目标函数 2 - 最大化 Xijtk
    z2 = np.max(Xijtk)
    
    # 目标函数 3 - Xijtk 变换
    def trans(a):
        if a > 0:
            return 1
        elif a == 0:
            return 0
        else:
            return -1
    
    z3 = np.sum(np.vectorize(trans)(Xijtk))
  