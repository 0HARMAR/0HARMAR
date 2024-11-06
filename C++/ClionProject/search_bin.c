/*#include <stdio.h>
#define MAXSIZE 10

int search_bin(int *a,int num)
{
    int start,end,midle;
    start=0;end=MAXSIZE-1;midle=(start+end)/2;
    while(midle)
    {
        if(num>a[midle]){start=midle+1;midle=(start+end)/2;}
        else if(num<a[midle]){end=midle-1;midle=(start+end)/2;}
        else return midle;
    }
}
int main()
{
    int a[MAXSIZE];
    for(int i=0;i<10;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("%d", search_bin(a,20));
}*/
