- __name__：每个 Python 模块都有一个内置的属性 __name__。当你直接运行一个模块时，__name__ 的值被设置为 "__main__"；如果该模块是被导入到其他模块中，则 __name__ 的值是模块的名称。\
- if __name__ == "__main__":：这行代码用于检查当前模块是否是主程序。如果是，那么就执行下面的代码块；如果这个模块被导入到其他模块中，则不会执行这个代码块。

例如直接执行下面的程序
```python
# my_module.py

def main():
    print("这是主程序")

if __name__ == "__main__":
    main()
```
会输出main打印的内容
***
而如果是其他模块引用
```python
# another_module.py

import my_module
```
**则不会输出任何内容，因为此时的__name__的值是another_module.py**