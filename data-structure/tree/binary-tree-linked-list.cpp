#include <iostream>
#include <cmath>

template <typename T>
class TreeNode {
public:
    T data;
    TreeNode<T>* left;
    TreeNode<T>* right;
    TreeNode<T>* parent;

    TreeNode(int data) : data(data), left(nullptr), right(nullptr), parent(nullptr) {

    }
};


template <typename T>
class ListNode {
public:
    T data;
    ListNode* prev;
    ListNode* next;

    ListNode(T data) : data(data), prev(nullptr), next(nullptr) {
    }
};

template <typename T>
class DoubleLinkedList {
public:
    ListNode<T>* head;
    ListNode<T>* tail;

    DoubleLinkedList() : head(nullptr), tail(nullptr) {

    }

    ~DoubleLinkedList() {
        ListNode<T>* current = head;
        ListNode<T>* next = current->next;

        while (current != nullptr) {
            next = current->next;
            delete current;
            current = next;
        }
    }

    void add(T data) {
        ListNode<T>* newNode = new ListNode<T>(data);

        if (this->head == nullptr) {
            this->head = newNode;
            this->tail = newNode;
        } else {
            this->tail->next = newNode;
            newNode->prev = this->tail;
            this->tail = newNode;
        }

    }
};



template <typename T>
class BinaryTree {
private:
    TreeNode<T>* root;

    void printElement(TreeNode<T>* node, int level, T* elements, int* isFill) {
        if (node == nullptr) {
            return;
        }

        elements[level] = node->data;
        isFill[level] = 1;

        printElement(node->left, 2 * level, elements, isFill);
        printElement(node->right, 2 * level + 1, elements, isFill);
    }

    int getHeight(TreeNode<T>* node) {
        if (node == nullptr) {
            return 0;
        }

        int l_height = this->getHeight(node->left);
        int r_height = this->getHeight(node->right);

        return (l_height > r_height) ? l_height + 1 : r_height + 1;
    }

    void preOrder(TreeNode<T>* node) {
        if(node == nullptr) {
            return;
        }

        std::cout << node->data << " ";
        preOrder(node->left);
        preOrder(node->right);
    }


    void postOrder(TreeNode<T>* node) {
        if(node == nullptr) {
            return;
        }

        postOrder(node->left);
        postOrder(node->right);
        std::cout << node->data << " ";
    }

    void inOrder(TreeNode<T>* node) {
        if(node == nullptr) {
            return;
        }

        inOrder(node->left);
        std::cout << node->data << " ";
        inOrder(node->right);
    }


public:
    BinaryTree() : root(nullptr) {
    }

    ~BinaryTree() {
        delete root;
    }

    void insertNode(TreeNode<T>* node, TreeNode<T>* parent) {
        if (parent == nullptr) {
            if (this->root == nullptr) {
                this->root = node;
            } else {
                throw std::out_of_range("Parent node is null");
            }
        } else {
            if (parent->left == nullptr) {
                parent->left = node;
                node->parent = parent;
            } else if (parent->right == nullptr) {
                parent->right = node;
                node->parent = parent;
            } else {
                throw std::out_of_range("Parent node is full");
            }
        }
    }

    void printTree() {
        int arraySize = ((int)std::pow(2, this->getHeight()));

        T* elements = new T[arraySize];
        int* isFill = new int[arraySize];

        for (int i = 0; i < arraySize; i++) {
            elements[i] = 0;
            isFill[i] = 0;
        }

        this->printElement(root, 1, elements, isFill);

        for (int i = 1; i < arraySize; i++) {

            if (isFill[i]) {
                std::cout << elements[i];
            } else {
                std::cout << "X";
            }

            if (std::log(i + 1) / std::log(2) == (int)(std::log(i + 1) / std::log(2))) {
                std::cout << std::endl;
            }
        }

        std::cout << std::endl;

        delete[] elements;
        delete[] isFill;
    }

    TreeNode<T>* getRoot() {
        return root;
    }

    int getHeight() {
        if(root == nullptr) {
            return 0;
        } else {
            return this->getHeight(root);
        }
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

template <typename T, typename U>
class HelperClass {
private:
    DoubleLinkedList<T>* list;
    bool (*filterNode)(TreeNode<T>*);
    U (*func)(DoubleLinkedList<T>*);

public:

    HelperClass(bool (*filterNode)(TreeNode<T>*), U (*func)(DoubleLinkedList<T>*))
    : filterNode(filterNode), func(func) {
        list = new DoubleLinkedList<T>();
    }

    void preOrder(TreeNode<T>* node) {
        if(node == nullptr) {
            return;
        } else {
            if(filterNode(node)) {
                list->add(node->data);
            }

            preOrder(node->left);
            preOrder(node->right);
        }
    }

    U calculate(BinaryTree<T>* tree) {
        this->preOrder(tree->getRoot());
        return func(list);
    }
};



int main() {

    BinaryTree<int> tree;

    TreeNode<int>* node1 = new TreeNode<int>(1);
    TreeNode<int>* node2 = new TreeNode<int>(2);
    TreeNode<int>* node3 = new TreeNode<int>(3);
    TreeNode<int>* node4 = new TreeNode<int>(4);
    TreeNode<int>* node5 = new TreeNode<int>(5);
    TreeNode<int>* node6 = new TreeNode<int>(6);
    TreeNode<int>* node7 = new TreeNode<int>(7);
    TreeNode<int>* node8 = new TreeNode<int>(8);

    tree.insertNode(node1, nullptr);
    tree.insertNode(node2, node1);
    tree.insertNode(node3, node1);
    tree.insertNode(node4, node2);
    tree.insertNode(node5, node2);
    tree.insertNode(node6, node5);
    tree.insertNode(node7, node3);
    tree.insertNode(node8, node3);


    std::cout << "Height: " << tree.getHeight() << std::endl;

    tree.printTree();

    tree.preOrder();
    std::cout << std::endl;

    tree.postOrder();
    std::cout << std::endl;

    tree.inOrder();
    std::cout << std::endl;
    std::cout << std::endl;

    std::cout << "Sum of all nodes: " << (new HelperClass<int, int>([](TreeNode<int>* node) {
        return true;
    }, [](DoubleLinkedList<int>* list) {
        ListNode<int>* current = list->head;
        int sum = 0;

        while (current != nullptr) {
            sum += current->data;
            current = current->next;
        }

        return sum;
    }))->calculate(&tree) << std::endl;


    std::cout << "Sum of even nodes: " << (new HelperClass<int, double>([](TreeNode<int>* node) {
        return node->data % 2 == 0;
    }, [](DoubleLinkedList<int>* list) {
        ListNode<int>* current = list->head;
        double sum = 0;

        while (current != nullptr) {
            sum += current->data;
            current = current->next;
        }

        return sum;
    }))->calculate(&tree) << std::endl;

    std::cout << "Sum of nodes of which parent value is even: " << (new HelperClass<int, double>([](TreeNode<int>* node) {
        return node->parent && node->parent->data % 2 == 0;
    }, [](DoubleLinkedList<int>* list) {
        ListNode<int>* current = list->head;
        double sum = 0;

        while (current != nullptr) {
            sum += current->data;
            current = current->next;
        }

        return sum;
    }))->calculate(&tree) << std::endl;

    std::cout << "Average of Tree: " << (new HelperClass<int, double>([](TreeNode<int>* node) {
        return true;
    }, [](DoubleLinkedList<int>* list) {
        ListNode<int>* current = list->head;
        int count = 0;
        double sum = 0;

        while (current != nullptr) {
            sum += current->data;
            count++;
            current = current->next;
        }

        return sum / count;
    }))->calculate(&tree) << std::endl;

    std::cout << "Average of Tree: " << (new HelperClass<int, int>([](TreeNode<int>* node) {
        return true;
    }, [](DoubleLinkedList<int>* list) {
        ListNode<int>* current = list->head;
        int count = 0;
        double sum = 0;

        while (current != nullptr) {
            sum += current->data;
            count++;
            current = current->next;
        }

        return (int)(sum / count);
    }))->calculate(&tree) << std::endl;

    return 0;
}