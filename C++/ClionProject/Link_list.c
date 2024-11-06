#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
typedef struct Node{
    int data;
    struct Node* next;
}Node,*LinkList;

typedef struct LinkStack{
    int data;
    struct LinkStack*next;
}LStack,*LinkStack;

void init_link_stack(LinkStack *LS){
    *LS=NULL;
}

void delete(LinkList link_list,int mink,int maxk){
    LinkList L=link_list->next;
    LinkList pre=link_list;
    while(L&&L->data<maxk){
        if(L->data>mink){
            pre->next=L->next;
            LinkList temp=L;
            L=L->next;
            free((LinkList)temp);
        } else{
            pre=pre->next;
            L=L->next;
        }
    }
}

void push(LinkStack *LS,int data){  //将元素压入栈
    LinkStack linkstack=(LinkStack) malloc(sizeof (LStack));
    linkstack->data=data;
    linkstack->next=*LS;
    *LS=linkstack;
}

void pop(LinkStack* LS,int *x){  //弹出栈顶元素
    LinkStack ls=*LS;
    *x=ls->data;
    (*LS)=(*LS)->next;
    free((LinkStack)(ls));
}
void creat_LinkList_R(Node** Head,int n){
    Node *temp=(Node*) malloc(sizeof (Node));
    *Head=temp;
    (*Head)->next=NULL;
    Node *r=*Head;
    int x;
    for(int i=0;i<n;i++){
        Node *temp=(Node*) malloc(sizeof (Node));
        r->next=temp;
        scanf("%d",&x);
        temp->data=x;
        r=temp;
    }
    r->next=NULL;
}

void display_link_list(Node* Head){
    Head=Head->next;
    while(Head){
        printf("%d",Head->data);
        Head=Head->next;
    }
}

void insert(LinkList L,int data,int i){
    LinkList LL=(LinkList) malloc(sizeof (Node));
    LL->data=data;
    LinkList prior=L;
    int count=1;
    L=L->next;
    while(count!=i){  //找到第i个节点的前驱指针
        prior=prior->next;
        count++;
    }
    LL->next=prior->next;
    prior->next=LL;
}

void reverse(LinkList link_list){
    LinkList pre=link_list->next;
    LinkList p=pre->next;
    LinkList temp_pre=pre->next;
    LinkList temp_p=p->next;
    link_list->next=p;
    p->next=pre;
    pre->next=NULL;
    p=temp_p;
    pre=temp_pre;
    while(p){
        temp_p=p->next;
        temp_pre=p;
        link_list->next=p;
        p->next=pre;
        p=temp_p;
        pre=temp_pre;
    }
}

void MergeGather(LinkList pa,LinkList *pb,LinkList *pc){
    *pc=pa;
    pa=pa->next;
    LinkList pb1=(*pb)->next;
    LinkList pc1=(*pc);
    while (pa&&pb1){
        if(pa->data==pb1->data)
        {
            pc1->next=pa;
            pc1=pa;
            pa=pa->next;
            pb1=pb1->next;
        }
        else if(pa->data<pb1->data){
            pa=pa->next;
        }
        else{
            pb1=pb1->next;
        }
    }
    pc1->next=NULL;  //pc1指向尾节点，所以要把尾指针设为空
}
int main(){
    LinkList head,pa,pb,pc;
    //creat_LinkList_R(&head,6);
    //insert(head,100,3);
    //delete(head,3,10);
    creat_LinkList_R(&pa,5);
    creat_LinkList_R(&pb,5);
    MergeGather(pa,&pb,&pc);
    //reverse(head);
    display_link_list(pc);
}
