/*#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
typedef int ElemType;
typedef struct DouNode{
    int data;
    struct Node* prior;
    struct Node* next;
}DouNode,*DouLinkList;

void creat_DouLinkList(DouLinkList * Head,int n){
    DouLinkList DLL=(DouLinkList) malloc(sizeof (DouNode));
    *Head=DLL;
    (*Head)->prior=NULL;
    DouLinkList r=(*Head);  //…Ë¡¢Œ≤÷∏’Î
    for(int i=0;i<n;i++){
        DouLinkList dll=(DouLinkList) malloc(sizeof (DouNode));
        r->next=dll;
        dll->prior=r;
        dll->next=NULL;
        scanf("%d",&(dll->data));
        r=r->next;
    }
}

void display_link_list(Node* Head){
    Node *Head_=Head->next;
    while(Head_->next!=NULL){
        printf("%d",Head_->data);
        Head_=Head_->next;
    }
}*/