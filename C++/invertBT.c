#include <stdio.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* invertTree(struct TreeNode* root) {
    if (root->left == NULL && root->right == NULL)
    return;
    else
    {
        struct TreeNode * temp = root->left;
        root -> left = root -> right;
        root -> right = temp;
        invertTree(root->left);
        invertTree(root->right);
    }
}