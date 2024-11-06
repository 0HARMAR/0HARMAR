/*#include <stdio.h>
#include <malloc.h>
#include <stdbool.h>

#define  MaxVexNum   20     //最大顶点数目
typedef struct
{    int  arcs[MaxVexNum][MaxVexNum];
    int  vexnum, arcnum;
}AMGraph;

void create_matrix(AMGraph *amGraph)
{
    int v1,v2;
    int ret;
    for(int i=0;i< amGraph->arcnum;i++)
    {
        ret=scanf("%d %d",&v1,&v2);
        amGraph->arcs[v1][v2]=1;amGraph->arcs[v2][v1]=1;
    }
}

void display_matrix(AMGraph *amGraph)
{
    for(int i=0;i<amGraph->vexnum;i++)
    {
        for(int j=0;j<amGraph->vexnum;j++)
        {
            printf("%d",amGraph->arcs[i][j]);
        }
        printf("\n");
    }
}
void DFS(AMGraph amGraph,int *is_passed,int row_index)
{
    if(row_index==0){printf("%d",row_index);is_passed[row_index]=1;}
    else if(is_passed[row_index]!=1){printf(" %d",row_index);is_passed[row_index]=1;}
    for(int i=0;i<amGraph.vexnum;i++)
    {
        if(amGraph.arcs[i][row_index]!=0&&!is_passed[i])
        {
            printf(" %d",i);
            is_passed[i]=1;
            DFS(amGraph,is_passed,i);
        }
    }
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
int main()
{
    AMGraph amGraph={{{0}},0,0};
    int is_passed[MaxVexNum]={0};
    int num_connect_component=0;
    scanf("%d %d",&amGraph.vexnum,&amGraph.arcnum);
    getchar();
    create_matrix(&amGraph);
    while(find_start(is_passed,amGraph.vexnum)!=-1)
    {
        DFS(amGraph,is_passed, find_start(is_passed,amGraph.vexnum));
        num_connect_component++;
    }
    printf("\n%d\n",num_connect_component);
    printf("%d",amGraph.arcnum);
}*/