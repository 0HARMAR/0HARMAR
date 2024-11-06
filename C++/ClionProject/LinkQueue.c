#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
typedef struct QNode {
    char data;
    struct QNode *next;
} QNode;

typedef struct {
    QNode *front;
    QNode *rear;
} LinkQueue;

void init_LinkQueue(LinkQueue *LQ) {
    LQ->front = LQ->rear = (QNode*)malloc(sizeof(QNode));
    LQ->front->next = NULL;
}

void in_LinkQueue(LinkQueue *LQ, char data) {
    QNode* s = (QNode*)malloc(sizeof(QNode));
    s->next = NULL;
    s->data = data;
    LQ->rear->next = s;
    LQ->rear = s;
}

bool out_LinkQueue(LinkQueue *LQ){
    if(LQ->front->next==NULL)return false;
    LQ->front->next=LQ->front->next->next;
    return true;
}

bool is_Null(LinkQueue LQ){
    if(LQ.front->next==NULL)return true;
    else return false;
}

char head_queue(LinkQueue LQ){
    return LQ.front->next->data;
}
void display(LinkQueue LQ) {
    QNode *head = LQ.front->next;
    while (head) {
        printf("%c", head->data);
        head = head->next;
    }
}

int main() {
    LinkQueue LQ;
    init_LinkQueue(&LQ);
    char c[100];
    char *p=c;
    scanf("%s",c);
    while(*p!='#'){
        in_LinkQueue(&LQ,*p);
        p++;
    }
    if(is_Null(LQ)){
        printf("Head:NULL\nPop:NULL");
    }
    printf("Head:%c", head_queue(LQ));
    printf("\n");
    printf("Pop:");
    while (!is_Null(LQ)){
        printf("%c", head_queue(LQ));
        out_LinkQueue(&LQ);
    }
    //display(LQ);
}
