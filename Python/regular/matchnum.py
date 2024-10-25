import re
result = re.match(r'\d+', '123abc')
if result:
    print(result.group())  # 输出: 123

result = re.match(r'\d+','abc123')
if result:
    print(result.group()) # output none
