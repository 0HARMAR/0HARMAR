import re

pattern = r'a' # 匹配字符‘a'

text = "apple"

result = re.match(pattern,text)

print(f"匹配结果: {result.group()}") # output 'a'