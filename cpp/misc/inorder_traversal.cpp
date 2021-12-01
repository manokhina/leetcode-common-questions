 #include <iostream>
 #include <vector>
 using namespace std;
 
 // Definition for a binary tree node.
 struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> nodes = {};
        inorder(root, nodes);
        return nodes;   
    }

    void inorder(TreeNode* root, vector<int>& v) {
        if (root == nullptr) return;
        inorder(root->left, v);
        v.push_back(root->val);
        inorder(root->right, v);
    }
};

int main() {
    TreeNode* left;
    left->val = 2;

    TreeNode* right;
    right->val = 3;

    TreeNode* rt;
    rt->val = 1;
    rt->left = left;
    rt->right = right;
    Solution solution;
    vector<int> result = solution.inorderTraversal(rt);
    for (auto& r : result) {
        std::cout << r;
    }
    return 0;
}