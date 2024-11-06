#include <stdio.h>

int main() {
#ifdef __linux__
    printf("IN LINUX\n");
#else
    printf("OTHERS\n");
#endif
    return 0;
}

