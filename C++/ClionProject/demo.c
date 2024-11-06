#include <stdio.h>
#include <unistd.h>

extern void print();

int (*fp)(int,int);
int add(int a, int b) {
    return a + b;
}
int (*fp)(int,int)=add;
int main()
{
   print(); 
   print();
   printf("%d",fp(1,3));
}
