import pandas as pd
import numpy as np
from scipy.optimize import linprog

# 读取2023年的农作物种植和相关统计数据
data_2023 = pd.read_excel('mathmodel/C题/附件2.xlsx')

# 假设数据结构如下
# data_2023 = {
#     'crop': ['wheat', 'corn', 'rice', 'vegetable', 'mushroom'],
#     'expected_sales': [1000, 800, 600, 2000, 1500],
#     'production_cost': [300, 350, 250, 200, 150],
#     'yield_per_acre': [1500, 1400, 1200, 1000, 800],
#     'selling_price': [2, 2.5, 3, 4, 5]
# }

# 自定义变量
years = list(range(2024, 2031))
acres = 1201  # 总耕地面积
fields_count = 34  # 地块数量
crops = data_2023['crop'].to_list()
expected_sales = data_2023['expected_sales'].to_list()
production_cost = data_2023['production_cost'].to_list()
yield_per_acre = data_2023['yield_per_acre'].to_list()
selling_price = data_2023['selling_price'].to_list()

# 建立决策变量，数量为每个作物在每年所种植的面积
num_vars = len(crops) * len(years)
c = np.zeros(num_vars)

# 构建目标函数系数：种植成本
for i in range(len(crops)):
    for j in range(len(years)):
        c[i * len(years) + j] = production_cost[i]

# 不等式约束：每年种植面积限制
A_ub = np.zeros((1, num_vars))
b_ub = np.zeros(1)
A_eq = np.zeros((1, num_vars))
b_eq = np.zeros(1)

for j in range(len(years)):
    for i in range(len(crops)):
        A_ub[0, i * len(years) + j] = 1
    b_ub[0] = acres

# 进入总产量和销售约束
for j in range(len(years)):
    A_eq_row = np.zeros(num_vars)
    for i in range(len(crops)):
        A_eq_row[i * len(years) + j] = yield_per_acre[i]  # 总产量
    A_eq[j] = A_eq_row
    b_eq[j] = sum(expected_sales)  # 需满足的销售量

# 优化模型：超出部分滞销造成浪费
result1_1 = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, method='highs')

# 提取结果
def extract_results(result, crops, years):
    planting_scheme = np.zeros((len(crops), len(years)))
#见完整版
