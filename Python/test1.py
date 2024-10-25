import random

"""it's seed test
"""


# 设置随机数种子
random.seed(12)

# 生成一系列随机数
print(random.random())  # 0.6394267984578837
print(random.randint(1, 10))  # 2
print(random.choice(['apple', 'banana', 'cherry']))  # 'banana'

# 重新设置种子，生成的随机数序列将与之前的相同
random.seed(12)
print(random.random())  # 0.6394267984578837
print(random.randint(1, 10))  # 2
print(random.choice(['apple', 'banana', 'cherry']))  # 'banana'
