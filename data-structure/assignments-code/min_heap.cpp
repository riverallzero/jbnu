#include <iostream>
#include <cmath>

template<typename T>
class TreeNode {
public:
    T data;
    TreeNode<T> *left;
    TreeNode<T> *right;
    TreeNode<T> *parent;

    TreeNode(int data) : data(data), left(nullptr), right(nullptr), parent(nullptr) {

    }
};


template<typename T>
class ListNode {
public:
    T data;
    ListNode *prev;
    ListNode *next;

    ListNode(T data) : data(data), prev(nullptr), next(nullptr) {
    }
};

template<typename T>
class DoubleLinkedList {
public:
    ListNode<T> *head;
    ListNode<T> *tail;

    DoubleLinkedList() : head(nullptr), tail(nullptr) {

    }

    ~DoubleLinkedList() {
        ListNode<T> *current = head;
        ListNode<T> *next = current->next;

        while (current != nullptr) {
            next = current->next;
            delete current;
            current = next;
        }
    }

    void add(T data) {
        ListNode<T> *newNode = new ListNode<T>(data);

        if (this->head == nullptr) {
            this->head = newNode;
            this->tail = newNode;
        } else {
            this->tail->next = newNode;
            newNode->prev = this->tail;
            this->tail = newNode;
        }

    }

    void remove(ListNode<T> *node) {
        if (node == head && node == tail) {
            head = tail = nullptr;
        } else if (node == head) {
            head = head->next;
            head->prev = nullptr;
        } else if (node == tail) {
            tail = tail->prev;
            tail->next = nullptr;
        } else {
            node->prev->next = node->next;
            node->next->prev = node->prev;
        }
        delete node;
    }
};


template<typename T>
class MinHeap {
private:
    TreeNode<T> *root;
    DoubleLinkedList<TreeNode<T> *> nodeList;
    int nodeCount;

    void printHeap(TreeNode<T> *node, int level, T *elements, int *isFill) {
        if (node == nullptr) {
            return;
        }

        elements[level] = node->data;
        isFill[level] = 1;

        printHeap(node->left, 2 * level, elements, isFill);
        printHeap(node->right, 2 * level + 1, elements, isFill);
    }

    int height(TreeNode<T> *node) {
        if (node == nullptr) {
            return 0;
        }

        int l_height = this->height(node->left);
        int r_height = this->height(node->right);

        return (l_height > r_height) ? l_height + 1 : r_height + 1;
    }

    void preOrder(TreeNode<T> *node, T *elements, int &index) {
        if (node == nullptr) {
            return;
        }

        elements[index++] = node->data;
        preOrder(node->left, elements, index);
        preOrder(node->right, elements, index);
    }

    void postOrder(TreeNode<T> *node, T *elements, int &index) {
        if (node == nullptr) {
            return;
        }

        postOrder(node->left, elements, index);
        postOrder(node->right, elements, index);
        elements[index++] = node->data;
    }

    void inOrder(TreeNode<T> *node, T *elements, int &index) {
        if (node == nullptr) {
            return;
        }

        inOrder(node->left, elements, index);
        elements[index++] = node->data;
        inOrder(node->right, elements, index);
    }

    TreeNode<T> *getParent() {
        if (nodeCount == 0)
            return nullptr;

        int parentIndex = (nodeCount - 1) / 2;

        ListNode<TreeNode<T> *> *current = nodeList.head;

        for (int i = 0; i < parentIndex; ++i) {
            current = current->next;
        }
        return current->data;
    }

    void heapifyUpstream(TreeNode<T> *node) {
        while (node->left != nullptr) {
            TreeNode<T> *smallestChild = node->left;
            if (node->right != nullptr && node->right->data < node->left->data) {
                smallestChild = node->right;
            }
            if (node->data <= smallestChild->data) {
                break;
            }
            std::swap(node->data, smallestChild->data);
            node = smallestChild;
        }
    }


public:
    MinHeap() : root(nullptr), nodeCount(0) {

    }

    ~MinHeap() {
        delete root;
    }

    void heapify() {
        heapifyUpstream(root);
    }

    void insert(T value) {
        TreeNode<T> *node = new TreeNode<T>(value);
        nodeList.add(node);

        if (height() == 0) {
            if (this->root == nullptr) {
                this->root = node;
            } else {
                throw std::out_of_range("Parent node is null");
            }
        } else {
            TreeNode<T> *parent = getParent();
            node->parent = parent;

            if (parent->left == nullptr) {
                parent->left = node;
            } else if (parent->right == nullptr) {
                parent->right = node;
            } else {
                throw std::out_of_range("Parent node is full");
            }
        }
        nodeCount++;
        heapify();
    }

    T get() {
        if (nodeCount == 0) {
            throw std::out_of_range("Heap is empty");
        }

        T rootValue = root->data;

        if (nodeCount == 1) {
            delete root;
            root = nullptr;
            nodeList.remove(nodeList.head);
            nodeCount--;
            std::cout << "[get] Root Value: " << rootValue << std::endl;
            return rootValue;
        }

        TreeNode<T> *lastNode = nodeList.tail->data;
        root->data = lastNode->data;

        if (lastNode->parent->left == lastNode) {
            lastNode->parent->left = nullptr;
        } else {
            lastNode->parent->right = nullptr;
        }

        nodeList.remove(nodeList.tail);
        delete lastNode;

        nodeCount--;

        heapify();

        std::cout << "[get] Root Value: " << rootValue << std::endl;
        return rootValue;
    }

    void printElement(const std::string &order) {
        T *elements = new T[nodeCount];
        int index = 1;

        if (order == "inorder") {
            inOrder(root, elements, index);
        } else if (order == "preorder") {
            preOrder(root, elements, index);
        } else if (order == "postorder") {
            postOrder(root, elements, index);
        } else {
            throw std::out_of_range("Only accept inorder, preorder, postorder!");
        }

        std::cout << "[" << order << "] ";
        for (int i = 1; i < nodeCount + 1; i++) {
            std::cout << elements[i];

            if (i != nodeCount) {
                std::cout << " => ";
            }
        }
        std::cout << std::endl;

        delete[] elements;
    }

    void printTree() {
        int arraySize = ((int) std::pow(2, this->height()));

        T *elements = new T[arraySize];
        int *isFill = new int[arraySize];

        for (int i = 0; i < arraySize; i++) {
            elements[i] = 0;
            isFill[i] = 0;
        }

        this->printHeap(root, 1, elements, isFill);

        std::cout << "----tree----\n";
        for (int i = 1; i < arraySize; i++) {

            if (isFill[i]) {
                std::cout << elements[i];
            } else {
                std::cout << "X";
            }

            if (std::log(i + 1) / std::log(2) == (int) (std::log(i + 1) / std::log(2))) {
                std::cout << std::endl;
            }
        }

        std::cout << "------------" << std::endl;

        delete[] elements;
        delete[] isFill;
    }

    int height() {
        if (root == nullptr) {
            return 0;
        } else {
            return this->height(root);
        }
    }

    int size() {
        return nodeCount;
    }

    void preOrder() {
        this->preOrder(root);
    }

    void postOrder() {
        this->postOrder(root);
    }

    void inOrder() {
        this->inOrder(root);
    }
};


int main() {
    MinHeap<int> minheap;

    minheap.insert(3);
    minheap.insert(4);
    minheap.insert(1);
    minheap.insert(5);
    minheap.insert(6);
    std::cout << "Size: " << minheap.size() << std::endl;
    std::cout << "Height: " << minheap.height() << std::endl;
    minheap.printTree();
    minheap.printElement("inorder");

    minheap.get();
    minheap.printTree();

    minheap.insert(7);
    minheap.printTree();
    minheap.printElement("postorder");

}