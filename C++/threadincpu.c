#include "macrobox.h"

MAIN{
    setbuf(stdout,NULL);
    int past = sched_getcpu();
    printint(past);
    while(1)
    {
        int current = sched_getcpu();
        if (current != past){
            printint(current);
            past = current;
        }
    }
}