def simple_generator():
    yield 1
    yield 2
    yield 3

# 使用生成器
gen = simple_generator()

# 迭代生成器
for value in gen:
    print(value)

#......................................................
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 使用生成器
fib_gen = fibonacci()

# 打印前10个斐波那契数
for _ in range(10):
    print(next(fib_gen))

# generator is a function that will save the local state?
