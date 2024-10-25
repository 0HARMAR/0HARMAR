import re
result = re.search(r'\d+', 'def123abc')
if result:
    print(result.group())  # 输出: 123
