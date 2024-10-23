#include <iostream>

template <typename T>
class Node {
private:
    T data;
    Node *next;

public:
    T getData() const {
        return this->data;
    }

    Node* getNext() const {
        return this->next;
    }

    void setData(T data) {
        this->data = data;
    }

    void setNext(Node* next) {
        this->next = next;
    }
};

template <typename T>
class LinkedList {
private:
    Node<T>* head;

public:
    LinkedList() : head(nullptr) {}
    ~LinkedList() {
        Node<T>* p = head;
        while (p != nullptr) {
            Node<T>* next = p->getNext();
            delete p;
            p = next;
        }
    }

    void add(T data) {
        Node<T>* newNode = new Node<T>();
        newNode->setData(data);
        newNode->setNext(nullptr);

        if (head == nullptr) {
            head = newNode;
        } else {
            Node<T>* p = head;
            while (p->getNext() != nullptr) {
                p = p->getNext();
            }
            p->setNext(newNode);
        }
    }

    void remove() {
        if (head == nullptr) {
            return;
        }

        Node<T>* p = head;
        Node<T>* prev = nullptr;
        while (p->getNext() != nullptr) {
            prev = p;
            p = p->getNext();
        }

        if (prev == nullptr) {
            head = nullptr;
        } else {
            prev->setNext(nullptr);
        }

        delete p;
    }

    void printState() const {

        Node<T>* p = head;
        while (p != nullptr) {
            std::cout << p->getData() << "( << " << p << " ) -> ";
            p = p->getNext();
        }
        std::cout << std::endl;
    }

    bool contains(T value) {
        Node<T>* p = head;
        while (p != nullptr) {
            if (p->getData() == value) {
                return true;
            }
            p = p->getNext();
        }
        return false;
    }
};

int main() {
    LinkedList<int> list;

    list.add(1);
    list.add(2);
    list.add(30);
    list.add(4);
    list.add(5);

    list.printState();

    list.remove();
    list.printState();

    std::cout << std::boolalpha;
    std::cout << list.contains(3) << std::endl;
}
