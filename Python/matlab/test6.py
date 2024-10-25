import math

# 定义指标体系
def warmth_index(length, diameter):
    # 计算纤维的横截面积 (单位：cm^2)
    cross_sectional_area = math.pi * (diameter / 2) ** 2
    # 假设的热导率基准值 (单位：W/mK)
    k = 1e-7
    # 计算纤维的热导率 (单位：W/mK)
    thermal_conductivity = k / cross_sectional_area
    # 计算纤维的热阻值 (单位：K/W)
    thermal_resistance = cross_sectional_area / k
    # 计算纤维的总热导传系数 (单位：W/mK)
    total_thermal_conductivity = thermal_conductivity / (density * (length *(1e3)* cross_sectional_area))
    # 计算纤维的CLO值
    clo_value = thermal_resistance / 0.155
    # 纤维厚度
    fiber_thickness = diameter  # 单位：cm
    # 纤维密度 (单位：g/cm^3)
    fiber_density = density

    # 返回指标值
    return thermal_conductivity, thermal_resistance, total_thermal_conductivity, clo_value, fiber_thickness, fiber_density

# 计算棉花的保暖能力
cotton_length = 2.8  # 单位：cm
cotton_diameter = 0.002  # 单位：cm (20微米)
density = 1.54  # 单位：g/cm^3
cotton_thermal_conductivity, cotton_thermal_resistance, cotton_total_thermal_conductivity, cotton_clo_value, cotton_fiber_thickness, cotton_fiber_density = warmth_index(cotton_length, cotton_diameter)
print("棉花的热导率为：", cotton_thermal_conductivity, "W/mK")
print("棉花的热阻值为：", cotton_thermal_resistance, "K/W")
print("棉花的总热导传系数为：", cotton_total_thermal_conductivity, "W/mK")
print("棉花的CLO值为：", cotton_clo_value)
print("棉花的纤维厚度为：", cotton_fiber_thickness, "cm")
print("棉花的纤维密度为：", cotton_fiber_density, "g/cm^3")


print('/n')
# 计算羽绒的保暖能力
down_length = 1.7  # 单位：cm
down_diameter = 0.0015  # 单位：cm (15微米)
density=0.8
down_thermal_conductivity, down_thermal_resistance, down_total_thermal_conductivity, down_clo_value, down_fiber_thickness, down_fiber_density = warmth_index(down_length, down_diameter)
print("羽绒的热导率为：", down_thermal_conductivity, "W/mK")
print("羽绒的热阻值为：", down_thermal_resistance, "K/W")
print("羽绒的总热导传系数为：", down_total_thermal_conductivity, "W/mK")
print("羽绒的CLO值为：", down_clo_value)
print("羽绒的纤维厚度为：", down_fiber_thickness, "cm")
print("羽绒的纤维密度为：", down_fiber_density, "g/cm^3")
