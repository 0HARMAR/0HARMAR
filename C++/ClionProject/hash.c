/*#include <stdio.h>
#include <stdbool.h>
#include <malloc.h>
typedef struct hash_node{
    int data;
    struct hash_node* next;
}Hnode;

typedef struct hashTable{
    Hnode *head;
    int length;
}hashTable;

int divisor;

bool is_prime(int number) {
    if (number <= 1)
        return false;
    if (number <= 3)
        return true;
    if (number % 2 == 0 || number % 3 == 0)
        return false;
    for (int i = 5; i * i <= number; i += 6) {
        if (number % i == 0 || number % (i + 2) == 0)
            return false;
    }
    return true;
}
int hash(int data)
{
    return data%divisor;
}

void find_divisor(int num){
    while(!is_prime(num+1)){num++;}
    divisor=num+1;
}

void create_hash_table(hashTable* HT,int *a,int num){
    int is_exist[100]={0};
    (*HT).length=divisor;
    (*HT).head=(Hnode*) malloc(sizeof (Hnode)*divisor);
    for(int i=0;i<divisor;i++){
        (*HT).head[i].next=NULL;
    }
    for(int i=0;i<num;i++)
    {
        if(is_exist[hash(a[i])])
        {
            Hnode *p=&((*HT).head[hash(a[i])]);
            while(p){if(p->next==NULL)break;p=p->next;}
            p->next=(Hnode*) malloc(sizeof (Hnode));
            p->next->data=a[i];
            p->next->next=NULL;
        }
        else{(*HT).head[hash(a[i])].data=a[i];is_exist[hash(a[i])]=1;}
    }
}

int search(int value,hashTable HT){
    if(HT.head[hash(value)].next==NULL)return HT.head[hash(value)].data;
    else
    {
        Hnode *p=&HT.head[hash(value)];
        while(p->next&&p->data!=value)p=p->next;
        return p->data;
    }
}
int main()
{
    int a[10],num;
    hashTable HT;
    for(int i=0;i<10;i++){scanf("%d",&a[i]);if(a[i]==-1){num=i;find_divisor(num);break;}}
    create_hash_table(&HT,a,num);
    printf("%d",search(8,HT));
}*/
