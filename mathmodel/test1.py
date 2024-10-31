import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
import random
import seaborn as sns
 
# 读取农作物信息（面积、作物类型、单价、产量等）
land_data = pd.read_excel('mathmodel/C题/附件1.xlsx')
production_data = pd.read_excel('处理后的文件.xlsx')
 
# 地块面积信息
area = land_data['地块面积/亩'].values
 
# 2023年农作物信息，包括单价、种植成本、产量等
crop_data = production_data[['作物类型', '亩产量/斤', '销售单价/(元/斤)', '种植成本/(元/亩)']].set_index('作物类型')

# 将相关列转换为数值类型
crop_data['亩产量/斤'] = pd.to_numeric(crop_data['亩产量/斤'], errors='coerce')
crop_data['销售单价/(元/斤)'] = pd.to_numeric(crop_data['销售单价/(元/斤)'], errors='coerce')
crop_data['种植成本/(元/亩)'] = pd.to_numeric(crop_data['种植成本/(元/亩)'], errors='coerce')

# 从crop_data提取变量
yield_per_acre = crop_data['亩产量/斤'].values
price_per_ton = crop_data['销售单价/(元/斤)'].values
cost_per_acre = crop_data['种植成本/(元/亩)'].values


sales_expectation = [81, 85, 112, 101, 107, 84, 103, 109, 111, 90, 115, 85, 90, 114, 100, 116, 96, 104, 
                     87, 112, 118, 89, 119, 109, 98, 102, 82, 93, 100, 88, 95, 83, 113, 88, 86, 80, 
                     110, 103, 119, 85, 87, 103, 115, 80, 91, 98, 95, 119, 110, 99, 110, 105, 88, 119, 
                     110, 80, 119, 91, 93, 98, 90, 120, 96, 106, 109, 101, 93, 104, 113, 96, 82, 98, 
                     120, 109, 112, 113, 105, 94, 106, 105, 101, 102, 101, 92, 119, 80, 107, 113, 97, 
                     113, 83, 80, 85, 112, 120, 90, 104, 102, 80, 117, 116, 90, 90, 111, 84, 102, 95,111,
                    121,120,110]

 
# 变量数量
num_land_blocks = len(area)  # 地块数量

print("Number of land blocks",num_land_blocks)
num_crops = len(crop_data)   # 作物种类数量

print(f"Number of crops: {num_crops}")
 
# 遗传算法相关参数
population_size = 50
generations = 100
mutation_rate = 0.01
 
# 初始化种群
def init_population(size):
    return np.random.rand(size, num_land_blocks, num_crops)
 
def fitness(individual):
    profit = 0
    for i in range(num_land_blocks):
        for j in range(num_crops):
            planted_area = individual[i, j] * area[i]
            production = planted_area * yield_per_acre[j]
            
            # 检查生产量是否在销售期望范围内
            if production <= sales_expectation[j]:
                profit += production * price_per_ton[j] - planted_area * cost_per_acre[j]
            else:
                surplus = production - sales_expectation[j]
                # 确保价格计算中不出现无效操作
                price_adjusted = price_per_ton[j] / 2
                profit += sales_expectation[j] * price_per_ton[j] + surplus * price_adjusted - planted_area * cost_per_acre[j]
            if not np.isnan(profit):
                print(type(profit), profit)
    return profit


 
# 变异操作
def mutate(individual):
    if np.random.rand() < mutation_rate:
        i = np.random.randint(num_land_blocks)
        j = np.random.randint(num_crops)
        individual[i, j] = np.random.rand()
    return individual
 
def selection(population):
    selected = []
    population_flat = population.reshape(len(population), -1)  # 将多维数组展平为一维
    for _ in range(len(population)):
        # 从展平的种群中随机选择两个个体
        indices = np.random.choice(len(population), size=2, replace=False)
        competitors = population_flat[indices]
        # 选择适应度更高的个体
        best_competitor = max(competitors, key=lambda x: fitness(x.reshape(num_land_blocks, num_crops)))
        selected.append(best_competitor.reshape(num_land_blocks, num_crops))
    return np.array(selected)

# 交叉操作
def crossover(parent1, parent2):
    # 随机选择一个交叉点
    point = np.random.randint(1, num_land_blocks * num_crops - 1)
    
    # 创建子代
    child1 = parent1.copy()
    child2 = parent2.copy()
    
    # 交换交叉点后的基因
    child1.flat[point:], child2.flat[point:] = parent2.flat[point:], parent1.flat[point:]
    
    return child1, child2


# 主遗传算法过程
def genetic_algorithm():
    population = init_population(population_size)
    best_solution = None
    best_fitness = 0
    fitness_history = []
 
    for generation in range(generations):
        population = selection(population)
        new_population = []
 
        # 交叉产生新个体
        for i in range(0, len(population), 2):
            parent1 = population[i]
            parent2 = population[min(i+1, len(population)-1)]
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
 
        population = np.array(new_population)
 
        # 记录最佳个体
        gen_best = max(population, key=fitness)
        gen_best_fitness = fitness(gen_best)
        fitness_history.append(gen_best_fitness)
 
        if gen_best_fitness > best_fitness:
            best_solution = gen_best
            best_fitness = gen_best_fitness
 
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")
 
    return best_solution, fitness_history
 
# 运行遗传算法
best_solution, fitness_history = genetic_algorithm()
 
# 总利润随代数变化趋势
plt.figure(figsize=(10, 6))
plt.plot(fitness_history, label='Total Profit')
plt.xlabel('Generations')
plt.ylabel('Profit')
plt.title('Total Profit Over Generations')
plt.legend()
plt.grid(True)
plt.show()
 
# 各地块的最佳作物种植方案
def plot_solution(solution):
    plt.figure(figsize=(12, 8))
    sns.heatmap(solution, annot=True, fmt=".2f", cmap='Blues', xticklabels=crop_data.index, yticklabels=land_data['地块名称'])
    plt.title("Optimal Crop Distribution Across Lands")
    plt.xlabel("Crops")
    plt.ylabel("Land Blocks")
    plt.show()
 
# 可视化最佳种植方案
plot_solution(best_solution)