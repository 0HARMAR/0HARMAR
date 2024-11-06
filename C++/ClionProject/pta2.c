/*#include <stdio.h>
#include <malloc.h>
#include <stdbool.h>

#define   MaxVexNum  20    //最大顶点数
typedef  struct  ArcNode   //表结点定义
{
    int  adjvex;
    struct  ArcNode  *nextarc;
}ArcNode;
typedef  struct
{
    ArcNode  *vertices[MaxVexNum];
    int   vernum, arcnum;
}ALGraph;

int temp[MaxVexNum]={'\0'};
void create_ArcList(ALGraph* alGraph)
{
    int v1[MaxVexNum],v2[MaxVexNum];
    for(int i=0;i<alGraph->vernum;i++)
    {
        ArcNode *p=(ArcNode*) malloc(sizeof (ArcNode));
        p->adjvex=i;p->nextarc=NULL;
        alGraph->vertices[i]=p;
    }
    for(int k=0;k<alGraph->arcnum;k++)
        scanf("%d %d",&v1[k],&v2[k]);
    for(int j=0;j<alGraph->arcnum;j++)
    {
        ArcNode *arcNode=(ArcNode*) malloc(sizeof (ArcNode));
        if(alGraph->vertices[j]->nextarc==NULL)arcNode->nextarc=NULL;
        arcNode->nextarc=alGraph->vertices[v1[j]]->nextarc;arcNode->adjvex=v2[j];
        alGraph->vertices[v1[j]]->nextarc=arcNode;
    }
    for(int l=alGraph->arcnum-1;l>=0;l--)
    {
        ArcNode *arcNode=(ArcNode*) malloc(sizeof (ArcNode));
        if(alGraph->vertices[l]->nextarc==NULL)arcNode->nextarc=NULL;
        arcNode->nextarc=alGraph->vertices[v2[l]]->nextarc;arcNode->adjvex=v1[l];
        alGraph->vertices[v2[l]]->nextarc=arcNode;
    }
}

void display_adjList(ALGraph * alGraph)
{
    for(int i=0;i<alGraph->vernum;i++)
    {
        printf("%d",alGraph->vertices[i]->adjvex);
        ArcNode * p=alGraph->vertices[i]->nextarc;
        while(p){printf("%d",p->adjvex);p=p->nextarc;}
        printf("\n");
    }
}

void BFS(ALGraph* alGraph,int *is_passed,int size,int start)
{
    if(size==0)return;
    int Size;
    if(start!=-1)
    {
        printf("%d",start);is_passed[start]=1;
        ArcNode *p=alGraph->vertices[start]->nextarc;
        int count=0;
        for(int i=0;p;i++)
        {
            printf("%d",p->adjvex);is_passed[p->adjvex]=1;
            temp[i]=p->adjvex;
            p=p->nextarc;
            count++;
        }
        Size=count;
    } else
    {
        int Temp[MaxVexNum];int *P=Temp;
        for(int i=0;i<size;i++)
        {
            ArcNode *p=alGraph->vertices[temp[i]]->nextarc;
            while(p)
            {
                if(is_passed[p->adjvex]!=1)
                { printf("%d",p->adjvex);is_passed[p->adjvex]=1;*P=p->adjvex;P++;}
                p=p->nextarc;
            }
        }
        Size=P-Temp;
        for(int i=0;i<P-Temp;i++)
        {
            temp[i]=Temp[i];
        }
    }
    BFS(alGraph,is_passed,Size,-1);
}
int find_start(int * is_passed,int num_vertax)
{
    bool flag=0;
    for(int i=0;i<num_vertax;i++)
    {
        if(is_passed[i]==0)flag=1;
    }
    if(!flag)return -1;
    int min=0;
    for(int j=0;j<num_vertax;j++)
    {
        if(is_passed[j]==0){min=j;break;}
    }
    return min;
}
int main(){
    ALGraph alGraph;
    int is_passed[MaxVexNum]={0};
    int num_connect_component=0;
    scanf("%d %d",&alGraph.vernum,&alGraph.arcnum);
    create_ArcList(&alGraph);
    display_adjList(&alGraph);
    while(find_start(is_passed,alGraph.vernum)!=-1)
    {
        BFS(&alGraph,is_passed,1, find_start(is_passed,alGraph.vernum));
        num_connect_component++;
    }
    printf("\n%d\n",num_connect_component);
}*/
