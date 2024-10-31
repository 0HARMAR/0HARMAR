#include <stdio.h>
#include <stdlib.h>

int main() {
    const char *home = getenv("PATH");
    if (home) {
        printf("HOME: %s\n", home);
    } else {
        printf("HOME not set.\n");
    }
    return 0;
}
