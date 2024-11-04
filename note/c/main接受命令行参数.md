实例程序
```c
int main(int argc, char *argv[]) {
    printf("总共有 %d 个命令行参数:\n", argc);
    
    for (int i = 0; i < argc; i++) {
        printf("参数 %d: %s\n", i, argv[i]);
    }

    return 0;
}
```
- argc：表示命令行参数的数量，包括程序名称在内。例如，如果你运行 ./program arg1 arg2，则 argc 的值为 3。
- argv：是一个字符串数组，包含每个命令行参数。argv[0] 是程序名称，argv[1] 是第一个参数，以此类推。
