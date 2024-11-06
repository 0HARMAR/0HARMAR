#include<stdio.h>

#define MAXSIZE 50     // MAXSIZE为最大数据元素数目
typedef int ElemType;
typedef struct
{  ElemType  r[MAXSIZE +1];    // r[0]闲置或另作它用
   int  length;
}SqList;

int main()
{
    SqList SL={0};
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",&(SL.r[i+1]));
        SL.length++;

    }

}
