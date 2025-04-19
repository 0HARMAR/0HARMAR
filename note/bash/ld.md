### 基本用法
ld -o program program.o

### 参数详解
- -Ttext=
**指定程序要加载的内存地址，ld据此计算出程序中要访问的地址**

- --oformat=
**指定链接产生的程序格式，例如**
1. binary
纯二进制格式 

### 链接器符号解释
__bss_start: bss段开始地址
_end/end : bss段结束地址
__TMC_END__ ： 事务内存结束地址。TMC ：Transactional Memory Clones 