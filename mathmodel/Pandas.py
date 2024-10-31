import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('mathmodel/C题/附件1.xlsx', sheet_name='乡村的现有耕地')

# 操作数据
print(df.head())

# 保存到 Excel 文件
df.to_excel('output.xlsx', index=False)
