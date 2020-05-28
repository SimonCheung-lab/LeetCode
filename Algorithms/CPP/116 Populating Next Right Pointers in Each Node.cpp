/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if (root == NULL) {
            return NULL;
        }
        std::vector<Node*> nodes;
        nodes.push_back(root);
        connect(nodes);
        return root;
    }
    void connect(std::vector<Node*> nodes) {
        if (nodes.size() == 0) {
            return;
        }
        std::vector<Node*> subLevel;
        for (int i = 0; i < nodes.size(); ++i) {
            if (i + 1 < nodes.size()) {
                nodes[i]->next = nodes[i + 1];
            }
            if (nodes[i]->left) {
                subLevel.push_back(nodes[i]->left);
            }
            if (nodes[i]->right) {
                subLevel.push_back(nodes[i]->right);
            }
        }
        nodes.back()->next = NULL;
        connect(subLevel);
    }
};


# recursion
class Solution {
public:
    Node* connect(Node* root) {
        if (root == NULL) {
            return NULL;
        }
        Node* left = root->left;
        Node* right = root->right;
        while (left && right) {
            left->next = right;
            left = left->right;
            right = right->left;
        }
        connect(root->left);
        connect(root->right);
        return root;
    }
};
