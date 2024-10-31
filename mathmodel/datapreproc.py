import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('mathmodel/C题/附件1.xlsx', sheet_name='乡村的现有耕地')

# 操作数据
# 累加指定列的前10行数据
column_sum = df['地块面积/亩'].iloc[:34].sum()

# 输出累加结果
print(f"列 'column_name' 的前10行累加结果是: {column_sum}")


# 保存到 Excel 文件
df.to_excel('output.xlsx', index=False)
