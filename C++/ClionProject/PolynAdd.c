/*#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

typedef struct PNode{
    float coef;  //系数
    int expn;  //指数
    struct PNode *next;  //指针域
}PNode,*Polynomial;

void creat_polynomial(Polynomial *P,int n){
    (*P)=(Polynomial) malloc(sizeof (PNode));
    (*P)->next=NULL;
    for(int i=0;i<n;i++){
        Polynomial s=(Polynomial) malloc(sizeof (PNode));
        scanf("%f %d",&s->coef,&s->expn);
        Polynomial pre,q;
        pre=(*P);
        q=(*P)->next;
        while(q&&q->expn<s->expn){
            pre=q;
            q=q->next;
        }
        s->next=q;
        pre->next=s;
    }
}

void AddPolyn(Polynomial PA,Polynomial PB){
    Polynomial p1=PA->next;
    Polynomial p2=PB->next;
    Polynomial p3=PA;  //也可以指向PB
    while(p1&&p2){
        if(p1->expn==p2->expn){  //指数相等
            int sum=p1->coef+p2->coef;
            if(sum!=0){  //系数不为0
                p1->coef=sum;
                p3->next=p1;
                p3=p1;
                p1=p1->next;
                Polynomial temp=p2;  //设置临时变量保存p2
                p2=p2->next;
                free((Polynomial)temp);
            }
            else  //系数为0，释放内存空间
            {
                Polynomial p1_=p1;
                Polynomial p2_=p2;
                p1=p1->next;
                p2=p2->next;
                free((Polynomial)p1_);
                free((Polynomial)p2_);
            }
        }
        else if(p1->expn<p2->expn){
             p3->next=p1;
             p3=p1;
             p1=p1->next;
        }
        else{
            p3->next=p2;
            p3=p2;
            p2=p2->next;
        }
    }
    p3->next=p1?p1:p2;
    free((Polynomial)PB);  //释放PB链表的头结点
}
void display(Polynomial P){
    P=P->next;
    while(P){
        printf("%fx%d,",P->coef,P->expn);
        P=P->next;
    }
}
int main(){
    Polynomial Pa,Pb;
    creat_polynomial(&Pa,2);
    creat_polynomial(&Pb,2);
    AddPolyn(Pa,Pb);
    display(Pa);
}*/