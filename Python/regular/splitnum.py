import re
result = re.split(r'\d+', 'abc123def456')
print(result)  # 输出: ['abc', 'def', '']
