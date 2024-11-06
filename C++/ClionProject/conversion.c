#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#define MAXSIZE 100
typedef struct {
    int *base;  //ջ��ָ��
    int *top;  //ջ��ָ��
    int stacksize;
}Stack;

void initstack(Stack* stack){
    stack->base= (Stack *)malloc(sizeof (int)*MAXSIZE);
    stack->top=stack->base;
    stack->stacksize=MAXSIZE;
}

void push(Stack* stack,int data){
    *stack->top++=data;
}

int pop(Stack* stack){  //����ջ��Ԫ��
    return *--stack->top;
}

void display_stack(Stack* stack){
    int * top=stack->top;
    for(;top!=stack->base;top--){
        if(*(top-1)>9){
            switch (*(top-1)) {
                case 10:
                    printf("A");
                    break;
                case 11:
                    printf("B");
                    break;
                case 12:
                    printf("C");
                    break;
                case 13:
                    printf("D");
                    break;
                case 14:
                    printf("E");
                    break;
                case 15:
                    printf("F");
                    break;
            }
        }
        else printf("%d",*(top-1));
    }
}
int main(){
    Stack * stack =(Stack *)malloc(sizeof(Stack));;
    initstack(stack);
    int num,system;
    scanf("%d",&num);scanf("%d",&system);
    printf("%d%d",num,system);
    while(num!=0){
        push(stack,num%system);
        num=num/system;
    }
    display_stack(stack);
}