#include<stdio.h>

int main()
{
    setbuf(stdout,NULL);  //set no buf
    printf("\033[31;40m红色文本，黑色背景\033[0m");  //escape code

    printf("\rhhhhhhhhhhhhhhhhhhhh,hello ,hello miao miao miao ");  //backspace
}