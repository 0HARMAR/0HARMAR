/*#include <stdio.h>
#include <malloc.h>
#include <stdbool.h>
#define MAXSIZE 100
typedef struct {
    int* data;  //存储空间的基地址
    int front;  //头指针
    int rear;  //尾指针
}SqQueue;

void init_SqQueue(SqQueue* SQ){
    SQ->data=(int*)malloc(MAXSIZE*sizeof (int));
    SQ->front=0;
    SQ->rear=0;
}

bool in_SqQueue(SqQueue* SQ,int data){
    if((SQ->rear+1)%MAXSIZE==SQ->front) return false;  //队满
    SQ->data[SQ->rear]=data;
    SQ->rear=(SQ->rear+1)%MAXSIZE;
    return true;
}

void display_SqQueue(SqQueue *SQ){
    int front=SQ->front;
    while(front!=SQ->rear){
        printf("%d",SQ->data[front]);
        front=(front+1)%MAXSIZE;
    }
    //printf("%d",SQ->data[front]);
}

bool out_SqQueue(SqQueue* SQ){
    if(SQ->front==SQ->rear) return false;   //队空
    SQ->front=(SQ->front+1)%MAXSIZE;
    return true;
}
int main(){
    SqQueue Sq;
    init_SqQueue(&Sq);
    in_SqQueue(&Sq,4);
    in_SqQueue(&Sq,7);
    in_SqQueue(&Sq,10);
    out_SqQueue(&Sq);
    display_SqQueue(&Sq);
}*/