#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

typedef struct BST
{
    int data;
    struct BST* Lp;
    struct BST* Rp;
} BST;

typedef struct BST* BSTP;

typedef struct {
    int data;
    struct CSnode*FC;
    struct CSnode*NS;
}CSnode;
int num=0;
int LEVEL=0;
BSTP getNewNode() {
    BSTP bstp = (BSTP)malloc(sizeof(BST));
    bstp->Lp = bstp->Rp = NULL;
    return bstp;
}

void insert(BSTP* root, int data) {
    if ((*root) == NULL) {
        (*root) = getNewNode();
        (*root)->data = data;
    }
    else if (data <= (*root)->data) {
        insert(&((*root)->Lp), data);
    }
    else {
        insert(&((*root)->Rp), data);
    }
}

void traversing_first(BSTP root) {  //先序遍历
    if (root != NULL) {
        printf("%d ", root->data);
        traversing_first(root->Lp);
        traversing_first(root->Rp);
    }
}

void traversing_midle(BSTP root){  //中序遍历
    if (root != NULL) {
        traversing_midle(root->Lp);
        printf("%d ", root->data);
        traversing_midle(root->Rp);
    }
}

int degree_of_1(BSTP bst){
    if(bst==NULL)return 0;
    if((bst->Lp==NULL&&bst->Rp!=NULL)||(bst->Lp!=NULL&&bst->Rp==NULL))
    {   num++;
    }
    degree_of_1(bst->Lp);
    degree_of_1(bst->Rp);
    return num;
}

int level_of_x(BSTP bstp,int level,int x){
    if(bstp==NULL)return 0;
    if(bstp->data==x)LEVEL=level;
    else
    {
        level_of_x(bstp->Lp,level+1,x);
        level_of_x(bstp->Rp,level+1,x);
    }
}

void find_level(CSnode *cs,int level){
    if(cs==NULL)return;
    if(level>LEVEL)LEVEL=level;
    find_level(cs->FC,level+1);
    find_level(cs->NS,level);
}

void create_BiT(BSTP root){
    int data;
    scanf("%d",&data);
    if(data==-1)root=NULL;
    else
    {
        BSTP bstp=(BSTP) malloc(sizeof (BST));
        bstp->data=data;
        bstp->Rp=bstp->Lp=NULL;
        create_BiT(bstp->Lp);
        create_BiT(bstp->Lp);
    }
}

int main() {
    BSTP root = NULL;
    insert(&root, 10);
    insert(&root, 15);
    insert(&root, 5);
    insert(&root, 20);
    insert(&root, 12);
    insert(&root, 17);
    insert(&root, 25);
    insert(&root,9);
    insert(&root,13);
    traversing_first(root);
    printf("\n");
    traversing_midle(root);
    printf("%d", degree_of_1(root));
    level_of_x(root,1,9);
    printf("%d",LEVEL);
    return 0;
}
