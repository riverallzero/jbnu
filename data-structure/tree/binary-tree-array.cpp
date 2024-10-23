# include <iostream>

template <typename T>
class BinaryTree {
private:
    T* tree; // 이진트리 배열
    T* isFill; // 노드가 채워졌는지 여부
    int capacity; // 배열의 최대 크기
    int count; // 현재 노드의 수
    int lastNode; // 마지막 노드의 인덱스

public:
    BinaryTree(int capacity) : capacity(capacity), count(0), lastNode(0) {
        this->tree = new T[capacity + 1];
        this->isFill = new T[capacity + 1];

        for (int i = 0; i < capacity + 1; i++) {
            this->tree[i] = 0;
            this->isFill[i] = 0;
        }
    }

    ~BinaryTree() {
        delete[] tree;
        delete[] isFill;
    }

    bool isEmpty() const {
        return this->count == 0;
    }

    bool isFull() const {
        return count == capacity;
    }

    int getRoot() const {
        if(this->isEmpty())
            throw std::out_of_range("Tree is empty");

        return tree[1];
    }

    int getCount() const {
        return count;
    }

    int getHeight() const {
        return static_cast<int>(std::log(lastNode) / std::log(2));
    }

    void insertNode(int parent, T data) {
        if(this->isFull())
            throw std::out_of_range("Tree is full");

        if(parent == 0) {
            if(this->isFill[1]) {
                throw std::out_of_range("Root is already filled");
            }
            else {
                this->tree[1] = data;
                this->isFill[1] = 1;
                this->count++;
                this->lastNode = 1;
            }
        } else if(this->isFill[parent]) {
            if(parent * 2 <= this->capacity && !this->isFill[parent * 2]) {
                this->tree[parent * 2] = data;
                this->isFill[parent * 2] = 1;
                this->count++;
                this->lastNode = parent * 2;
            } else if(parent * 2 + 1 <= this->capacity && !this->isFill[parent * 2 + 1]) {
                this->tree[parent * 2 + 1] = data;
                this->isFill[parent * 2 + 1] = 1;
                this->count++;
                this->lastNode = parent * 2 + 1;
            } else {
                throw std::out_of_range("Parent node is already filled");
            }
        } else {
            throw std::out_of_range("Parent node does not exist");
        }
    }
};
