import re

pattern2 = r"^h.*o$"  # 匹配以 "h" 开头，以 "o" 结尾的字符串
text2 = "hello"
result2 = re.match(pattern2, text2)
print(f"元字符匹配: {result2.group()}")  # 输出: hello