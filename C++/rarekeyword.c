#include<stdio.h>

enum Color {  //type enum
    RED,
    GREEN,
    BLUE
};

//auto int num=1;  //failed
int main()
{
    //printf("%d",num);  //failed

    volatile int notuse=10;  //movl   $0xa,-0x4(%rbp) ;not optimized despite not use

    enum Color favorcolor=RED;
    printf("%d",favorcolor);  // 0
}