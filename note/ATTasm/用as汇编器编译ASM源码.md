# 编译
as -o program.o program.s
ld -o program program.o

# 运行
./program

### 添加调试信息
as -g -o program.o program.s