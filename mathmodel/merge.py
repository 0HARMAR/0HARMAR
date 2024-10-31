import pandas as pd

# 读取两张表
df1 = pd.read_excel('mathmodel/C题/附件1.xlsx')
df2 = pd.read_excel('mathmodel/C题/附件2.xlsx')

# 纵向合并
combined_df = pd.concat([df1, df2], ignore_index=True)

# 横向合并
combined_df1 = pd.concat([df1, df2], axis=1)

# 保存到新的 Excel 文件
combined_df.to_excel('mathmodel/C题/合并结果.xlsx', index=False)

combined_df1.to_excel('mathmodel/C题/合并结果1.xlsx', index=False)
