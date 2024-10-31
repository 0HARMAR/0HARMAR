#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define NUM_THREADS 10
#define SEMAPHORE_VALUE 3

sem_t semaphore;

void* task(void* arg) {
    int task_id = *((int*)arg);
    printf("Task %d is waiting for the semaphore.\n", task_id);
    
    // 获取信号量
    sem_wait(&semaphore);
    printf("Task %d has acquired the semaphore.\n", task_id);
    
    // 模拟任务执行
    sleep(2);
    
    printf("Task %d is releasing the semaphore.\n", task_id);
    // 释放信号量
    sem_post(&semaphore);
    
    printf("Task %d has released the semaphore.\n", task_id);
    free(arg);
    return NULL;
}

int main() {
    pthread_t threads[NUM_THREADS];
    
    // 初始化信号量
    sem_init(&semaphore, 0, SEMAPHORE_VALUE);
    
    for (int i = 0; i < NUM_THREADS; i++) {
        int* task_id = malloc(sizeof(int));
        *task_id = i;
        pthread_create(&threads[i], NULL, task, task_id);
    }
    
    // 等待所有线程完成
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }
    
    // 销毁信号量
    sem_destroy(&semaphore);
    
    printf("All tasks are completed.\n");
    return 0;
}
