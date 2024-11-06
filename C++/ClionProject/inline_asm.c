#include <stdio.h>

int main() {
    int a = 5, b = 3, result;

    asm("addl %%ebx, %%eax"
        : "=a" (result)     // 输出操作数
        : "a" (a), "b" (b)  // 输入操作数
    );

    asm volatile("call main");
    asm volatile("addl %%ebx,%%eax"
        : "=a" (a)  //output
        : "a" (result), "b" (b)  //input
        );
    printf("Result: %d a:%d b:%d\n", result,a,b);
    return 0;
}


