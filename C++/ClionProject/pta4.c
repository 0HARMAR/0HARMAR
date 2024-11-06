/*#include <stdio.h>
#include <malloc.h>
#define MAXSIZE 50
typedef int ElemType;
typedef  struct
{
  ElemType  *R;
  int  length;
} SSTable;

int SSearch(int data,SSTable * ssTable)
{
    int *p=ssTable->R;
    for(int i=0;i<ssTable->length;i++,p++)
    {
        if(*p==data)return i+1;
    }
    return -1;
}

int main()
{
    int len,data;
    SSTable ssTable;
    int *p=(int *) malloc(sizeof (int)*MAXSIZE);ssTable.length=0;ssTable.R=p;
    scanf("%d",&len);
    for(int i=0;i<len;i++)
    {
        scanf("%d",ssTable.R+i);
        ssTable.length++;
    }
    scanf("%d",&data);
    if(SSearch(data,&ssTable)==-1)printf("NOT FOUND");
    else
    printf("%d",SSearch(data,&ssTable));
}*/