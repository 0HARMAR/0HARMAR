import numpy as np

# 定义基础变量
d_str = """0.052 0.025 0.033 0.035 0.028 0.045
0.161 0.4 0.303 0.286 0.357 0.222
0.04 0.035 0.03 0.32 0.32 0.32
0.5 1.125 0.8 0.9 0.7 0.6
15 20 18 16 17 14
1.52 0.9 1.38 0.91 1.14 1.25"""
d_matrix = np.array([[round(float(x), 5) for x in line.split()] for line in d_str.split("\n")])
print("决策矩阵: \n", d_matrix)

# 正负理想解
solve_1 = np.array([0.052, 0.4, 0.03, 1.125, 20, 1.52])
solve_0 = np.array([0.025, 0.161, 0.32, 0.5, 14, 0.9])
print("正理想解: ", solve_1)
print("负理想解: ", solve_0)

# 第1步：指标归一化处理，采用极差变换法计算归一化矩阵
d_matrix_regular = np.abs((d_matrix - solve_1[:, np.newaxis]) / (solve_1 - solve_0)[:, np.newaxis]) # 采用numpy库的广播算法
print("归一化矩阵: \n", d_matrix_regular)

# 第2步：计算第j项指标下第i个样本值的比重（即每个元素除以该元素所在列的和）
p_matrix = d_matrix_regular / np.sum(d_matrix_regular, axis=0)
print("比重矩阵: \n", p_matrix)

# 第3步：计算第j列指标的熵值（公式中0ln0=0，为避免计算时出错，在计算ln0时，给矩阵赋一个极小的值）
e_vector = - np.sum(p_matrix * np.log(np.where(p_matrix == 0, 1e-10, p_matrix)), axis=0) / np.log(6.)
print("指标的熵值: ", e_vector)

# 第4步：计算各项指标的权重：

# 定义新的权重，其中 CLO 值的权重设定为0.3
new_weights = np.array([0.1, 0.1, 0.1, 0.3, 0.2, 0.2])
print("预设的权重: ", new_weights)

# 重新计算权重
w_vector = new_weights / np.sum(new_weights)
print("调整后的权重: ", w_vector)
