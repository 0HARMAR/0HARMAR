#include "thread.h"
#include "spin.c"

#define N 100000000

long sum = 0;
pthread_mutex_t lock_;

void Tsum() {
  for (int i = 0; i < N; i++) {
    asm volatile("lock addq $1, %0": "+m"(sum));  //implement exclusion by lock prefix
  }
}

void Tsum_() {
  for (int i = 0; i < N; i++) {
    lock();  //implement exclusion by spin lock
    sum++;
    unlock();
  }
}

void Tsum_P() {
  for (int i = 0; i < N; i++) {
    pthread_mutex_lock(&lock_);  //implement exclusion by pthread mutex
    sum++;
    pthread_mutex_unlock(&lock_);
  }
}

int main() {
  pthread_mutex_init(&lock_,NULL);

  //2 threads:25s ; 4 threads:1m54s 
  // create(Tsum_);
  // create(Tsum_);
  // create(Tsum_);
  // create(Tsum_);

  //
  create(Tsum_P);
  create(Tsum_P);
  join();
  printf("sum = %ld\n", sum);
}
