import pandas as pd

# 读取数据
crop_data = pd.read_excel('合并后的文件.xlsx')

# 提取每个价格字符串的前四个字符
def extract_first_number(price_range):
    # 确保 price_range 是字符串类型
    if isinstance(price_range, str):
        # 查找 '-' 的位置
        dash_index = price_range.find('-')
        if dash_index != -1:
            # 切片获取 '-' 前的部分，并取前4个字符
            min_price = price_range[:dash_index].strip()
            return min_price[:1]  # 保留前4个字符
    return ''  # 如果不是字符串或未找到 '-', 返回空字符串

# 应用提取函数
crop_data['销售单价/(元/斤)'] = crop_data['销售单价/(元/斤)'].apply(extract_first_number)

# 检查数据
print(crop_data['销售单价/(元/斤)'].head())

# 保存处理后的数据到新文件
crop_data.to_excel('处理后的文件.xlsx', index=False)
