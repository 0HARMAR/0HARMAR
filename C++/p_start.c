#include <stdio.h>

extern void _start(void);
extern char** environ;

int main() {
    printf("_start address: %p\n", (void *)&_start);
    printf("environ :%s",*environ);
    return 0;
}