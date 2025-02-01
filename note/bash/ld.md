### 基本用法
ld -o program program.o

### 参数详解
- -Ttext=
**指定程序要加载的内存地址，ld据此计算出程序中要访问的地址**

- --oformat=
**指定链接产生的程序格式，例如**
1. binary
纯二进制格式