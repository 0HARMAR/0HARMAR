#include <stdio.h>
#include "thread.h"
#define N 100000000

int xchg(volatile int *addr, int newval) {
    int result;
    asm volatile ("lock xchg %0, %1"
            : "+m"(*addr), "=a"(result) : "1"(newval));
    return result;
}

int locked = 0;
void lock() { while (xchg(&locked, 1)) ; }
void unlock() { xchg(&locked, 0); }

long sum = 0;

void Tsum() {
    for (int i = 0; i < N; i++) {
        lock();
        sum++;
        unlock();
    }
}

int main()
{
    create(Tsum);
    create(Tsum);
    join();
    printf("sum = %ld\n", sum);
}