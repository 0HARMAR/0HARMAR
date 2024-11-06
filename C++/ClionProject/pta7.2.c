/*#include<stdio.h>
#include<malloc.h>
#include <stdlib.h>
#include <time.h>
#include<stdbool.h>
typedef struct double_cycle_linklist_node {
    struct double_cycle_linklist_node* front;
    struct double_cycle_linklist_node* rear;
    int data;
} dc_linklist_node;

typedef struct double_cycle_linklist{
    int length;
    dc_linklist_node *head;
}double_cycle_linklist;

bool create_dclinklist(double_cycle_linklist * dcLL) {
    dc_linklist_node* Head = (dc_linklist_node*)malloc(sizeof(dc_linklist_node));
    Head->front = Head->rear = Head;
    (*dcLL).head= Head;(*dcLL).length=0;
    dc_linklist_node* r = Head;
    while (1) {
        int x;
        int ret=scanf("%d", &x);
        if(ret==-1)return false;
        getchar();
        if(x==-1) return true;
        dc_linklist_node* node = (dc_linklist_node*)malloc(sizeof(dc_linklist_node));
        r->rear = node;
        node->data = x;
        node->front = r;
        node->rear = Head;
        if (Head->rear == Head) Head->rear = node;
        Head->front = node;
        r = node;
        (*dcLL).length++;
    }
}

void display(double_cycle_linklist head) {
    printf("链表长:%d",head.length);
    dc_linklist_node* Head = head.head->rear;
    while (Head != head.head) {
        printf("%d ", Head->data);
        Head = Head->rear;
    }
}

void find (int index,double_cycle_linklist dcLL){
    if(index<=dcLL.length/2){
        dc_linklist_node *head=dcLL.head;
        int count=0;
        while(count!=index){head=head->front;count++;}
        printf("%d",head->data);
    }
    else
    {
        dc_linklist_node *head=dcLL.head->rear;
        int count=0;
        while(count!=(dcLL.length-index)){head=head->rear;count++;}
        printf("%d",head->data);
    }
}
int main() {
    int index;
    int ret=scanf("%d",&index);
    if(ret==-1){printf("NULL");return 0;}
    getchar();
    double_cycle_linklist  dcLL;
    bool state=create_dclinklist(&dcLL);
    printf("%s",state?"true":"false");
    if(index>=1&&index<=dcLL.length&&state)find(index,dcLL);
    else printf("NULL");
    return 0;
}*/
