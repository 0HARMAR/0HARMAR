/*#include <stdio.h>

int main() {
    int a = 10;
    int b = 20;
    int result;

    asm (
            "add %[input1], %[input2] \n\t"
            : [result] "=r" (result)
            : [input1] "r" (a), [input2] "r" (b)
    );

    printf("Result: %d\n", result);

    return 0;
}*/
