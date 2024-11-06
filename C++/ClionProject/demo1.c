#include <stdio.h>


void print()
{
    static int i=0;
    printf("hello%d",i);
    i++;
}
