#include<stdio.h>


int main()
{
    FILE *fp=fopen("signal.c","r");
    printf("%d",fp->_file);  //  file descrptor is 3
}