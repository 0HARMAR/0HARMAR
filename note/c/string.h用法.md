1. 字符串拼接strcat
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[50] = "Hello, ";
    char str2[] = "World!";
    
    strcat(str1, str2);  // 将 str2 拼接到 str1 后面
    printf("%s\n", str1);  // 输出: Hello, World!

    return 0;
}
```
- 注意，拼接的目标字符串要有足够的空间，strcat不会分配内存空间