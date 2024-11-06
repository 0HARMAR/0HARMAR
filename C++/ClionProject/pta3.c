/*0#include <stdio.h>
#include <stdlib.h>

// 定义 ElemType
typedef int ElemType;

// 定义 BSTNode 结构体
typedef struct BSTNode {
    ElemType data;
    struct BSTNode *lchild, *rchild;
} BSTNode, *BSTree;

// 创建新的节点
BSTree getNewNode() {
    BSTree bstp = (BSTree)malloc(sizeof(BSTNode));
    bstp->lchild = bstp->rchild = NULL;
    return bstp;
}

// 插入节点
void insert(BSTree* root, ElemType data) {
    if (*root == NULL) {
        *root = getNewNode();
        (*root)->data = data;
    } else if (data <= (*root)->data) {
        insert(&((*root)->lchild), data);
    } else {
        insert(&((*root)->rchild), data);
    }
}

// 先序遍历
void traversing_first(BSTree root) {
    if (root != NULL) {
        printf("%d ", root->data);
        traversing_first(root->lchild);
        traversing_first(root->rchild);
    }
}

// 中序遍历
void traversing_midle(BSTree root) {
    if (root != NULL) {
        traversing_midle(root->lchild);
        printf("%d ", root->data);
        traversing_midle(root->rchild);
    }
}

// 查找节点并获取其左孩子和右孩子的数据
void BT_search(BSTree root, ElemType data, int *lchild, int *rchild) {
    if (data == root->data) {
        *lchild = root->lchild ? root->lchild->data : -1;
        *rchild = root->rchild ? root->rchild->data : -1;
    } else if (data > root->data) {
        BT_search(root->rchild, data, lchild, rchild);
    } else {
        BT_search(root->lchild, data, lchild, rchild);
    }
}

int main() {
    BSTree root = NULL;
    insert(&root, 10);
    insert(&root, 15);
    insert(&root, 5);
    insert(&root, 20);
    insert(&root, 12);
    insert(&root, 17);
    insert(&root, 25);
    insert(&root, 9);
    insert(&root, 13);

    printf("Pre-order traversal: ");
    traversing_first(root);
    printf("\n");

    int lchild, rchild;
    BT_search(root, 20, &lchild, &rchild);
    printf("Left child of 20: %d, Right child of 20: %d\n", lchild, rchild);

    return 0;
}*/
