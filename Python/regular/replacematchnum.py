import re
result = re.sub(r'\d+', 'NUMBER', 'abc123def456')
print(result)  # 输出: abcNUMBERdefNUMBER
