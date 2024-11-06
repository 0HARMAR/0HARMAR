/*#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#define OK 1
#define ERROR 0
#define OVERFLOW -2
#define MAX_SIZE 10
typedef int Status;
typedef struct SqeList{
    int* data;
    int length;
}SqeList;

Status initList(SqeList* S){
    S->data=(int*)malloc(MAX_SIZE * sizeof(int));
    S->length=0;
    int x;
    scanf("%d",&x);
    for(int i=0;i<MAX_SIZE&&x!=-1;i++){
        S->data[i]=x;
        S->length++;
        scanf("%d",&x);
    }
}

void insert(SqeList* S,int position,int data){

    for(int i=S->length;i>position-1;i--){
        S->data[i]=S->data[i-1];
    }
    S->data[position-1]=data;
    S->length++;
}

void display(SqeList* S){
    for(int i=0;i<S->length;i++){
            printf("%d,%d/",(S->data[i]),i);
    }
}

int main(){
    SqeList SL;
    initList(&SL);
    insert(&SL,2,100);
    display(&SL);
}*/