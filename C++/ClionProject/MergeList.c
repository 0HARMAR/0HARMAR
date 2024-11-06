#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

typedef struct Node{
    int data;
    struct Node* next;
}Node,*LinkList;

void creat_LinkList(LinkList * Head,int n){
    LinkList temp=(Node*) malloc(sizeof (Node));
    *Head=temp;
    (*Head)->next=NULL;
    LinkList r=*Head;  //设置尾指针
    int x;
    for(int i=0;;i++){
        scanf("%d",&x);
        if(x==-1)break;
        LinkList temp=(LinkList) malloc(sizeof (Node));
        r->next=temp;
        temp->data=x;
        r=temp;
    }
    r->next=NULL;
}

void display_link_list(LinkList Head){
    Node *Head_=Head->next;
    while(Head_){
        if(Head_==Head->next)
        printf("%d",Head_->data);
        else printf(" %d",Head_->data);
        Head_=Head_->next;
    }
}

void MergeList(LinkList La,LinkList *Lb,LinkList *Lc){
    LinkList Lb1=*Lb;
    LinkList Lc1=La;  //新链表在La的基础上修改
    *Lc=La;
    La=La->next;
    Lb1=Lb1->next;
    while(La&&Lb1){
        if(La->data>Lb1->data){
            Lc1->next=Lb1;
            Lc1=Lb1;
            Lb1=Lb1->next;
        }
        else if(La->data==Lb1->data)
        {
            Lc1->next=La;
            Lc1=Lc1->next;
            La=La->next;
        }
        else
        {
            Lc1->next=La;
            Lc1=La;
            La=La->next;
        }
    }
    Lc1->next=La?La:Lb1;
    free((LinkList)*Lb);
}
int main(){
    LinkList L1,L2,L3;
    creat_LinkList(&L1,3);
    creat_LinkList(&L2,5);
    if(L1->next==NULL&&L2->next==NULL)printf("NULL");
    MergeList(L1,&L2,&L3);
    display_link_list(L3);
}