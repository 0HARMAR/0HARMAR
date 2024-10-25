# 原始列表，包含不可变对象（整数和字符串）
original_list = [1, 2, "hello"]

# 浅拷贝
copied_list = original_list[:]

# 修改原列表中的元素
original_list[0] = 100

print("原始列表:", original_list)    # 输出: [100, 2, 'hello']
print("拷贝列表:", copied_list)     # 输出: [1, 2, 'hello']

copied_list_multi2 = original_list * 2

print("原始列表*2:",copied_list_multi2)

copied_list_multi2[3] = 200

print("原始列表*2:",copied_list_multi2)

dp = [[0 for _ in range(2)] for _ in range(3)]

dp[1][1] = 1

print(dp)

dp = [[0] * 2 for _ in range(3)]

dp[1][0] = 1

print(dp)