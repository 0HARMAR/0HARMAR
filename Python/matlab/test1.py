# 导入所需的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 建立指标体系的函数
def index_system(thermal_conductivity, thermal_resistance, thermal_conductivity_coefficient, density, thickness, weight, moisture_absorption, breathability):
    # 计算指标体系的加权平均值
    index = (thermal_conductivity + thermal_resistance + thermal_conductivity_coefficient + density + thickness + weight + moisture_absorption + breathability) / 8
    return index

# 定义保暖纤维的各项指标
thermal_conductivity = 0.5  //热导率
thermal_resistance = 0.7  //热阻值
thermal_conductivity_coefficient = 0.6  //热导系数
density = 0.8  //密度
thickness = 0.9  //厚度
weight = 0.7  //重量
moisture_absorption = 0.5  //吸湿性
breathability = 0.6  //透气性

# 调用函数计算指标体系的加权平均值
index = index_system(thermal_conductivity, thermal_resistance, thermal_conductivity_coefficient, density, thickness, weight, moisture_absorption, breathability)

# 输出指标体系的加权平均值
print("保暖纤维的指标体系加权平均值为：", index)
