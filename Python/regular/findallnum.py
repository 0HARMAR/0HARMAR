import re
results = re.findall(r'\d+', 'abc123def456')
print(results)  # 输出: ['123', '456']
