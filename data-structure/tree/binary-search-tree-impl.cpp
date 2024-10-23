#include <iostream>

template <typename T>
class TreeNode {
public:
    T data;
    TreeNode<T>* left;
    TreeNode<T>* right;
    TreeNode<T>* parent;

    TreeNode(T data) : data(data), left(nullptr), right(nullptr), parent(nullptr) {

    }
};


template <typename T>
class BinarySearchTree {
private:
    TreeNode<T>* root;


    void insertNode(TreeNode<T>*& subTree, T data) {
        if (subTree == nullptr) {
            subTree = new TreeNode<T>(data);
        } else if (subTree->data == data) {
            // Element already exists, do nothing to handle duplicates
            return;
        } else if (subTree->data > data) {
            if (subTree->left == nullptr) {
                TreeNode<T>* newNode = new TreeNode<T>(data);
                subTree->left = newNode;
                newNode->parent = subTree;
            } else {
                insertNode(subTree->left, data);
            }
        } else {
            if (subTree->right == nullptr) {
                TreeNode<T>* newNode = new TreeNode<T>(data);
                subTree->right = newNode;
                newNode->parent = subTree;
            } else {
                insertNode(subTree->right, data);
            }
        }
    }

    void printTree(TreeNode<T>* node) {
        if (node == nullptr) {
            return;
        }

        std::cout << "value: " << node->data << " (parent: " << (node->parent == nullptr ? "null" : std::to_string(node->parent->data)) << ") [left: " << (node->left == nullptr ? "null" : std::to_string(node->left->data)) << " - right: " << (node->right == nullptr ? "null" : std::to_string(node->right->data)) << "]" << std::endl;
        printTree(node->left);
        printTree(node->right);
    }

    TreeNode<T>* remove(TreeNode<T>*& subTree, T data) {
        if (subTree == nullptr) {
            return subTree;  // Element not found, return null
        } else if (data < subTree->data) {
            subTree->left = remove(subTree->left, data);  // Search in the left subtree
        } else if (data > subTree->data) {
            subTree->right = remove(subTree->right, data);  // Search in the right subtree
        } else {
            // Found the node with the value
            if (subTree->left == nullptr) {
                TreeNode<T>* temp = subTree->right;
                delete subTree;  // Delete the node
                return temp;  // Connect parent to right child
            } else if (subTree->right == nullptr) {
                TreeNode<T>* temp = subTree->left;
                delete subTree;  // Delete the node
                return temp;  // Connect parent to left child
            } else {
                // Node with two children, get the inorder successor (smallest in the right subtree)
                TreeNode<T>* temp = findMin(subTree->right);
                subTree->data = temp->data;  // Copy the inorder successor's data to this node
                subTree->right = remove(subTree->right, temp->data);  // Delete the inorder successor
            }
        }
        return subTree;  // Return the node pointer, which might have been updated
    }

    TreeNode<T>* findMin(TreeNode<T>* node) {
        while (node->left != nullptr) {
            node = node->left;
        }
        return node;
    }


    bool searchRecursive(TreeNode<T>* node, T data) {
        if (node == nullptr) {
            return false;
        }

        if (node->data == data) {
            return true;
        } else if (node->data > data) {
            return searchRecursive(node->left, data);
        } else {
            return searchRecursive(node->right, data);
        }
    }


public:

    BinarySearchTree() : root(nullptr) {

    }

    void insert(T data) {
        insertNode(root, data);
    }

    bool search(T data) {
        TreeNode<T>* current = root;

        while (current != nullptr) {
            if (current->data == data) {
                return true;
            } else if (current->data > data) {
                current = current->left;
            } else {
                current = current->right;
            }
        }

        return false;
    }

    bool searchRecursive(T data) {
        return searchRecursive(root, data);
    }

    void remove(T data) {
        this->remove(root, data);
    }


    void printTree() {
        printTree(root);
    }

};


int main() {
    BinarySearchTree<int> bst;

    bst.insert(10);
    bst.insert(20);
    bst.insert(5);
    bst.insert(15);
    bst.insert(25);


    bst.printTree();
    std::cout << std::endl;

    std::cout << "Searching for 15: " << bst.search(15) << std::endl;
    std::cout << "Searching for 100: " << bst.search(100) << std::endl;
    std::cout << "Searching for 5: " << bst.search(5) << std::endl;
    std::cout << std::endl;

    bst.remove(20);
    bst.printTree();
    std::cout << std::endl;

    bst.remove(10);
    bst.printTree();
    std::cout << std::endl;

    return 0;
}