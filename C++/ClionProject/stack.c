#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#define MAXSIZE 100
typedef struct {
    int *base;  //栈底指针
    int *top;  //栈顶指针
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

int pop(Stack* stack){  //弹出栈顶元素
    return *--stack->top;
}

void display_stack(Stack* stack){
    int * top=stack->top;
    for(;top!=stack->base;top--){
        printf("%d",*(top-1));
    }
}
int main(){
    Stack * stack =(Stack *)malloc(sizeof(Stack));;
    initstack(stack);
    for(int i=0;i<5;i++){
        push(stack,i);
    }
    int pop_data=pop(stack);
    printf("%d\n",pop_data);
    display_stack(stack);
}
