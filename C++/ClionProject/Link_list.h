#ifndef MY_FUNCTIONS_H
#define MY_FUNCTIONS_H

#include <stdio.h>

typedef struct Node_{
    int data;
    struct Node_* next;
    struct Node_*lchild;
    struct Node_*rchild;
}Node_,*LinkList_;
void display_link_list(LinkList_  Head){
    Head=Head->next;
    while(Head){
        printf("%d",Head->data);
        Head=Head->next;
    }
}
#endif