#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <sched.h>

int main() {
    int cpu_num = sched_getcpu();
    if (cpu_num == -1) {
        perror("sched_getcpu failed");
        return 1;
    }

    printf("Current thread is running on CPU: %d\n", cpu_num);

    return 0;
}
