/*#include<stdio.h>
#include<malloc.h>
#define MAXSIZE 10     // MAXSIZEΪ�������Ԫ����Ŀ
typedef int ElemType;
typedef struct
{  ElemType  *elem;
    int length;
} SqList;

void display(SqList Sq,int i){  //1��ʾbefore,0��ʾafter
    int count=0;
    ElemType *p=Sq.elem;
    if(i==1){
        printf("Before:");
    }
    else
    {
        printf("After:");
    }
    while(count<Sq.length){
        if(p==Sq.elem)
            printf("(%d",*p);
        else
            printf(",%d",*p);
        p++;
        count++;
    }
    printf(")");
}

int main (){
    SqList Sq;
    ElemType* p=(ElemType*)malloc(MAXSIZE*sizeof(ElemType));
    int n;
    int position;
    Sq.elem=p;
    Sq.length=0;
    scanf("%d",&n);
    while(Sq.length<n){
        scanf("%d",p++);
        (Sq.length)++;
    }
    scanf("%d",&position);
    display(Sq,1);
    printf("\n");
    if(position>n){
        printf("Delete position error!");
        return 0;
    }
    for (int j = position; j <= Sq.length - 1; j++)
        Sq.elem[j - 1] = Sq.elem[j];
    --Sq.length;
    display(Sq,0);
}*/
