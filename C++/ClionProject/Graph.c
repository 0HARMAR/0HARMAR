/*#include <stdio.h>
#include <malloc.h>
#include <stdbool.h>
typedef struct vertaxList{
    int length;
    char *vertax;
}vertaxList;

typedef struct edge{
    char end;
    char start;
    int weight;
}Edge;

typedef struct parent_list_node{
    char vertax;
    int index;
}PLnode;

typedef struct matrix{  //邻接矩阵
    int matrix[10][10];
    int length;
}matrix;

typedef struct adjListNode{
    int index;
    struct adjListNode*next;
}adjListNode;

typedef struct adjListHeadNode{  //邻接表头结点
    char data;
    adjListNode *next;
}adjListHeadNode;

typedef struct adjList{
    int length;
    adjListHeadNode *adjLHN;
}adjList;
void create_vList(vertaxList* v,int n){
    (*v).length=0;
    (*v).vertax=(char*) malloc(sizeof (char)*100);
    char *p=(*v).vertax;
    char x;
    for(int i=0;i<n;i++){
        scanf("%c",p);
        getchar();
        p++;
        (*v).length++;
    }
}

void display_vList(vertaxList v){
    char *p=v.vertax;
    printf("%d",v.length);
    for(int i=0;i<v.length;i++){
        printf("%c",*p);
        p++;
    }
}

void create_matrix(matrix* M,int n){
    (*M).length=n;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&(*M).matrix[i][j]);
        }
    }
}

void display_matrix(matrix M){
    int n=M.length;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            printf("%d ",M.matrix[i][j]);
        }
        printf("\n");
    }
}

void create_linklist(int i,adjListHeadNode* adjLHN){
    int index;
    adjListNode *r=NULL;  //尾指针
    scanf("%d",&index);
    if(index==-1)return;
    else{
        adjListNode* adjLN=(adjListNode*) malloc(sizeof (adjListNode));
        adjLN->index=index;
        adjLN->next=NULL;
        adjLHN[i].next=adjLN;
        r=adjLN;
    }
    while(1){
        scanf("%d",&index);
        if(index==-1)break;
        else
        {
            adjListNode* adjLN=(adjListNode*) malloc(sizeof (adjListNode));
            adjLN->index=index;
            adjLN->next=NULL;
            r->next=adjLN;
            r=adjLN;
        }
    }

}

void create_adjList(adjList* adjL,int n,vertaxList v){
    (*adjL).adjLHN=(adjListHeadNode*) malloc(sizeof (adjListHeadNode)*10);
    (*adjL).length=n;
    char* p=v.vertax;
    for(int i=0;i<n;i++,p++){   //初始化头结点数组
        (*adjL).adjLHN[i].data=(*p);
        (*adjL).adjLHN[i].next=NULL;
    }

    for(int i=0;i<n;i++){
        create_linklist(i,(*adjL).adjLHN);
    }
}

void display_adjL(adjList adjL){
    for(int i=0;i<adjL.length;i++){
        printf("%c",adjL.adjLHN[i].data);  //输出顶点
        adjListNode* adjLN=adjL.adjLHN[i].next;
        while(adjLN){
            printf("%d",adjLN->index);
            adjLN=adjLN->next;
        }
        printf("\n");
    }
}

void DFS(matrix M,vertaxList V,int index_row,int *is_passed){
    if(index_row==0&&is_passed[0]==0){printf("%c",V.vertax[index_row]);is_passed[0]=1;}
        for(int j=0;j<V.length;j++){
            if(M.matrix[j][index_row]!=0&&!is_passed[j])
            {
                printf("%c",V.vertax[j]);
                is_passed[j]=1;
                DFS(M,V,j,is_passed);
            }
        }
}

int find_index(char vertax,vertaxList V){
    if(vertax=='#')return -1;
    for(int i=0;i<V.length;i++){if(V.vertax[i]==vertax)return i;}
}

void adjDFS(adjList *adjL,char start,int *is_passed,vertaxList V)
{
    adjListNode *p=(*adjL).adjLHN[find_index(start,V)].next;
    printf("%c",start);
    is_passed[find_index(start,V)]=1;
    while(p)
    {
        if(is_passed[p->index]==1)p=p->next;
        else
        {
            adjDFS(adjL,V.vertax[p->index],is_passed,V);p=p->next;
        }
    }
}

void adjBFS(adjList *adjL,char start,int *is_passed,vertaxList V,int flag)
{
    adjListNode *p=(*adjL).adjLHN[find_index(start,V)].next;
    if(flag==0)
    {
        adjBFS(adjL,start,is_passed,V,1);
        while(p)
        {
            adjBFS(adjL,V.vertax[p->index],is_passed,V,1);
            p=p->next;
        }
        p=(*adjL).adjLHN[find_index(start,V)].next;
        while(p)
        {
            adjBFS(adjL,V.vertax[p->index],is_passed,V,0);
            p=p->next;
        }
    } else
    {
        if(is_passed[find_index(start,V)]==1);
        else
        {printf("%c",start);
            is_passed[find_index(start,V)]=1;}
        while(p)
        {
            if(is_passed[p->index]==1){p=p->next;continue;}
            printf("%c",V.vertax[p->index]);is_passed[p->index]=1;
            p=p->next;
        }
    }
}
void BFS(matrix M,vertaxList V){
    int is_passed[10]={0};
    for(int i=0;i<V.length;i++){
        if(is_passed[i]!=1){printf("%c",V.vertax[i]);is_passed[i]=1;}
        for(int j=0;j<V.length;j++){
            if(M.matrix[j][i]!=0&&is_passed[j]!=1){printf("%c",V.vertax[j]);is_passed[j]=1;}
        }
    }
}

bool in_linked(char *p,char vertax){
    while(*p!='\0'){if(vertax==*p)return true;p++;}
    return false;
}

void prim(matrix M,vertaxList V,char root,Edge * edge)
{
    char linked[10]={'\0'};char *p=linked;linked[0]=root;
    for(int i=0;i<V.length-1;i++)
    {
        p=linked;
        int min_weight=600000;
        if(i==0){edge[i].end=*p;edge[i].start='#';}
        while(*p!='\0')
        {
            int index=find_index(*p,V);
            for(int j=0;j<V.length;j++)
            {
                if(in_linked(linked,V.vertax[j]))continue;
                if(M.matrix[j][index]!=0&&M.matrix[j][index]<min_weight)
                {min_weight=M.matrix[j][index];edge[i+1].start=*p;edge[i+1].end=V.vertax[j];}
            }
            p++;
        }
        *p=edge[i+1].end;
    }
}

void CreatePList(PLnode* pLnode,Edge *edge,vertaxList V){
    for(int i=0;i<V.length;i++){
        pLnode[i].vertax=V.vertax[i];
        for(int j=0;j<V.length;j++)
            if(edge[j].end==V.vertax[i])
                pLnode[i].index= find_index(edge[j].start,V);
    }
}

void DisplayPList(PLnode* pLnode,vertaxList V){
    for(int i=0;i<V.length;i++){printf("%c%d",pLnode[i].vertax,pLnode[i].index);}
}
int main(){
    vertaxList V;
    matrix M;
}
*/