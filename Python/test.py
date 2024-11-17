import sys

# 打印当前路径列表
print("原始 sys.path:")
print("\n".join(sys.path))

# 指定需要保留的路径
valid_paths = [
    r"C:\Users\hemingyang\anaconda3\Lib\site-packages",
    r"C:\Users\hemingyang\anaconda3",
]

# 过滤多余路径
sys.path = [path for path in sys.path if path in valid_paths]

# 打印修改后的路径
print("\n修改后的 sys.path:")
print("\n".join(sys.path))

for path in valid_paths:
    sys.path.append(path)

print(sys.path)
