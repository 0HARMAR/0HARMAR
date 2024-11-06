#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

typedef struct LinkStack{
    int data;
    struct LinkStack*next;
}LStack,*LinkStack;

void init_link_stack(LinkStack *LS){
    *LS=NULL;
}

void push(LinkStack *LS,int data){  //将元素压入栈
    LinkStack linkstack=(LinkStack) malloc(sizeof (LStack));
    linkstack->data=data;
    linkstack->next=*LS;
    *LS=linkstack;
}

void pop(LinkStack* LS){  //弹出栈顶元素
    LinkStack ls=*LS;
    (*LS)=(*LS)->next;
    free((LinkStack)(*LS));
}

void display(LinkStack LS){
    while(LS->next!=NULL){
        printf("%d,",(LS->data));
        LS=LS->next;
    }
    printf("%d,",(LS->data));
}
int main(){
    LinkStack LS;
    init_link_stack(&LS);
    push(&LS,3);
    push(&LS,2);
    display(LS);
}