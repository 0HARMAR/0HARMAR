extern int _end;
#include <stdio.h>

int a;
int b;
int c;
int main(){
    printf("%x,%p",_end,&_end);
}