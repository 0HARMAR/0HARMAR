#include <stdio.h>
#include "thread.h"
#include <stdlib.h>
#include <time.h>

char seq[] = "123456789";

void Ta (){
    while (1){
    printf("thread a in cpu %d\n",sched_getcpu());
    sleep(1);
}
}

void Tb (){
    while (1){
    printf("thread b in cpu %d\n",sched_getcpu());
    sleep(2);
}
}

int main (){
    create(Ta);
    create(Tb);
}