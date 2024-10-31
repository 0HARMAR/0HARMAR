import numpy as np

# 定义初始数据
crops = ["小麦", "油菜", "水稻", "大豆", "玉米", "玉米间作大豆", "马铃薯", "绿肥"]
acre_revenue = [151.9, 68.8, 107.9, 109.3, 84.3, 81.0, 81.2, 50]  # 每种作物的亩收入 (元/亩)
acre_yield = [755, 222, 906, 186.3, 659, 564, 850, 3000]  # 每种作物的亩产量 (斤/亩)
initial_allocation = [4, 1.5, 3, 1, 2, 1.58, 0.8, 0.54]  # 初始估计解集 (亩)
total_land = 290  # 总耕地面积 (亩)

# 定义动态规划方程
def dynamic_programming(crops, acre_revenue, acre_yield, total_land):
    # 初始化收益和种植面积
    f = np.zeros(total_land + 1)
    allocation = np.zeros((len(crops), total_land + 1))

    # 动态规划计算
    for k in range(len(crops) - 1, -1, -1):
        for land in range(total_land + 1):
            max_revenue = 0
            for x in range(0, land + 1):  # 遍历每种作物的可能种植面积
                current_revenue = acre_revenue[k] * x + f[land - x]
                if current_revenue > max_revenue:
                    max_revenue = current_revenue
                    allocation[k, land] = x
            f[land] = max_revenue

    return f[total_land], allocation[:, total_land]

# 计算最佳方案
optimal_revenue, optimal_allocation = dynamic_programming(crops, acre_revenue, acre_yield, total_land)

# 输出结果
print(f"最大收益: {optimal_revenue:.2f} 元")
for i in range(len(crops)):
    print(f"{crops[i]}: {optimal_allocation[i]:.2f} 亩")
