#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#include <stdbool.h>

//结构体定义
typedef struct haffman_node{  //哈夫曼树节点
    char name;
    int weight;
    struct haffman_node* next;
    struct haffman_node*lchild;
    struct haffman_node*rchild;
}Hnode;

typedef struct code_table{  //编码表
    char name;
    char *code;
    int len;
}code_table;

void creat_haffman_linklist(Hnode**Head,int n);  //创建输入节点链表
void sort_haffman_linklist(Hnode *head);  //对输入节点排序
void display_haffman_linklist(Hnode *head);  //输出节点链表
void ChangeWeightList(Hnode *weight, Hnode *new_node);  //添加新节点后，对链表重新排序
void create_huffman_tree(Hnode *weight, Hnode **root);  //创建哈夫曼树
void traversing_first_haffman(Hnode *root);  //先序遍历哈夫曼树
void haffman_code(char name,char _1_or_0,char *code,Hnode *root);  //对每个字符编码
void code_string(char *start,code_table* codeTable,char *code);  //对给定字符串编码
char is_match(code_table *codeTable,char *start,char *end);  //对一段01序列译码
void decode(char *code,code_table *codeTable,char * string);  //对一段文本编码序列译码

bool is_code=false;
void creat_haffman_linklist(Hnode ** Head,int n){
    Hnode *temp=(Hnode *) malloc(sizeof (Hnode));
    *Head=temp;
    (*Head)->next=NULL;
    Hnode *r=*Head;
    int x;char name;
    for(int i=0;i<n;i++){
        Hnode *temp=(Hnode *) malloc(sizeof (Hnode));
        temp->lchild=temp->rchild=NULL;
        r->next=temp;
        scanf("%d:%c",&x,&name);
        temp->weight=x;
        temp->name=name;
        r=temp;
    }
    r->next=NULL;
}

void sort_haffman_linklist(Hnode *head)
{
    Hnode *p=(*head).next;
    while(p)
    {
        int min=p->weight;char min_name=p->name;Hnode *position=NULL;
        Hnode *p1=p->next;
        while(p1)
        {
            if(p1->weight<min)
            {min=p1->weight;min_name=p1->name;position=p1;}
            p1=p1->next;
        }
        if(position!=NULL){position->weight=p->weight;position->name=p->name;}
        p->weight=min;
        p->name=min_name;
        p=p->next;
    }
}

void display_haffman_linklist(Hnode *head)
{
    Hnode *p=head->next;
    while(p){printf("%d:%c",p->weight,p->name);p=p->next;}
}

void ChangeWeightList(Hnode *weight, Hnode *new_node) {
    weight->next = weight->next->next->next;
    Hnode *pre = weight;
    Hnode *p = weight->next;

    while (p) {
        if (new_node->weight <= weight->next->weight) {
            pre->next = new_node;
            new_node->next = p;
            return;
        }
        if (p->weight < new_node->weight) {
            pre = pre->next;
            p = p->next;
        } else {
            pre->next = new_node;
            new_node->next = p;
            return;
        }
    }

    pre->next = new_node;
}

void create_huffman_tree(Hnode *weight, Hnode **root) {
    if (weight->next == NULL) return;

    Hnode *p = weight->next;
    Hnode *first, *second;
    first=p;second=p->next;
    p=p->next->next;
    Hnode *new_node = (Hnode*)malloc(sizeof(Hnode));
    new_node->weight = first->weight + second->weight;
    new_node->lchild = first;
    new_node->rchild = second;
    new_node->name='#';
    new_node->next = NULL;

    if (!p) {
        *root = new_node;
        return;
    }

    ChangeWeightList(weight, new_node);
    create_huffman_tree(weight, root);
}

void traversing_first_haffman(Hnode *root) {
    if (root != NULL) {
        printf("%d %c\n", root->weight,root->name);
        traversing_first_haffman(root->lchild);
        traversing_first_haffman(root->rchild);
    }
}

void haffman_code(char name,char _1_or_0,char *code,Hnode *root)
{
    if(is_code)return;
    if(!root)return;
    if(root->name==name){*code=_1_or_0;*(code+1)='\0';is_code=true;return;}
    *code=_1_or_0;
    haffman_code(name,'0',code+1,root->lchild);
    haffman_code(name,'1',code+1,root->rchild);}

void code_string(char *start,code_table* codeTable,char *code)
{
    for(int i=0;*(start+i)!='\0';i++)
    {
        for(int j=0;j<26;j++)
        {
            if(codeTable[j].name==*(start+i))
            {
                for(int k=0;k<10;k++)
                {
                    if(codeTable[j].code[k]=='\0')break;
                    *code=codeTable[j].code[k];
                    code++;
                }
                break;
            }
        }
    }
}

char is_match(code_table *codeTable,char *start,char *end)
{
    char name='#';
    bool matched=false;
    for(int i=0;i<26;i++)
    {
        bool flag=true;
        if(matched)break;
        char *p=codeTable[i].code;
        for(int j=0;j<end-start;j++)
        {
            if(*p!=*(start+j)){flag=false;
                break;}
            p++;
        }
        if(flag)
        {
            if(p-codeTable[i].code==codeTable[i].len)
            {
                matched=true;
                name=codeTable[i].name;
            }
        }
    }
    return name;
}
void decode(char *code,code_table *codeTable,char * string)
{
    while(*code!='\0')
    {
        bool matched=false;
        int len;
        for(int i=0;i<6;i++)
        {
            if(matched)break;
            char is_match_=is_match(codeTable,code,code+3+i);
            if(is_match_=='#')continue;
            else
            {
                printf("%c",is_match_);
                matched=true;
                len=3+i;
                break;
            }
        }
        code=code+len;
    }
}
int main()
{
    Hnode *head;Hnode *root;
    int n; scanf("%d" ,&n);
    code_table codeTable[26];
    char string[50]={'\0'};char code[500]={'\0'};
    creat_haffman_linklist(&head,n);
    sort_haffman_linklist(head);//对节点排序
    create_huffman_tree(head,&root);
    traversing_first_haffman(root);
    for(int i=0;i<26;i++){  //字符编码
        is_code=false;
        char *code=(char*) malloc(sizeof (char)*10);
        haffman_code('A'+i,'#',code,root);
        codeTable[i].name='A'+i;codeTable[i].code=code+1;
    }
    for(int i=0;i<26;i++)  //count code len
    {
        char *start=codeTable[i].code;
        int count=0;
        while(*start!='\0'){count++;start++;}
        codeTable[i].len=count;
    }
    for(int i=0;i<26;i++)
    {
        printf("%c %s\n",codeTable[i].name,codeTable[i].code);
    }
    scanf("%s",string);
    code_string(string,codeTable,code);//字符串编码
    char * Code=code;
    printf("编码:");
    for(int i=0;i<500;i++)
    {
        if(*Code=='\0')break;
        printf("%c",*Code);
        Code++;
    }
    printf("\n译码:");
    decode(code,codeTable,string);//字符串译码
    printf("\n");
}


//输入序列26 64:A 13:B 22:C 32:D 103:E 21:F 15:G 47:H 57:I 1:J 5:K 32:L 20:M 57:N 63:O 15:P 1:Q 48:R 51:S 80:T 23:U 8:V 18:W 1:X 16:Y 1:Z


