/*#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#include <time.h>
#include <sys/time.h>
#include <stdbool.h>

typedef struct Node{
    int data;
    struct Node* next;
}Node,*LinkList;

LinkList p1Head;
void creat_LinkList_R(Node** Head){
    Node *temp=(Node*) malloc(sizeof (Node));
    *Head=temp;
    (*Head)->next=NULL;
    Node *r=*Head;
    int x;
    while(1){
        scanf("%d",&x);if(x==-1)break;
        Node *temp=(Node*) malloc(sizeof (Node));
        r->next=temp;
        temp->data=x;
        r=temp;
    }
    r->next=NULL;
}

int is_exist_in_linklist(int data,LinkList L){
    L=L->next;
    while(L){
        if(L->data==data)
            return 1;
        L=L->next;
    }
    return 0;
}
void MergeGather(LinkList p1,LinkList *p2,LinkList *p3){
    *p3=p1;  //在p1链表的基础上修改
    LinkList pb=(*p2);
    pb=pb->next;
    LinkList r=(*p3);
    while(r->next)  //找到尾指针
        r=r->next;
    while(pb){
        if(is_exist_in_linklist(pb->data,p1))
        {
            pb=pb->next;
        }
        else{
            r->next=pb;
            r=pb;
            pb=pb->next;
            r->next=NULL;  //尾指针的指针域设为空
        }
    }
}

bool find_intersection(LinkList p1,LinkList p2,LinkList *p3){
    if(!(p1&&p1->next&&p2&&p2->next))return false;
    p1=p1->next;
    p2=p2->next;
    int flag=0;
    while(p1&&p2)
    {
        if(p1->data>p2->data)p2=p2->next;
        else if(p1->data<p2->data)p1=p1->next;
        else
        {
            if(flag)printf(" %d",p1->data);
            else {printf("%d",p1->data);flag=1;}
            LinkList temp=p1->next;
            (*p3)=p1;
            p1->next=NULL;
            p1=temp;
            p2=p2->next;

        }
    }
    return true;
}
void display(LinkList L){
    if(L==p1Head)
        L=L->next;
    if(L==NULL){
        ;
    }
    printf("%d",L->data);
    display(L->next);  //递归
}

int main(){
    LinkList p1,p2,p3,p4;
    p4=NULL;
    creat_LinkList_R(&p1);
    p1Head=p1;
    creat_LinkList_R(&p2);
    bool state=find_intersection(p1,p2,&p4);
    if(!state||!p4)printf("NULL");
    //MergeGather(p1,&p2,&p3);
    //display(p3);
}*/
