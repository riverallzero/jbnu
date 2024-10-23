#include <iostream>
#include <stdexcept>

template <typename T>
class Node {
private:
    T value;
    Node* next;
    Node* prev;

public:

    Node(T value) {
        this->setValue(value);
        this->setNext(nullptr);
    }

    void setValue(T value) {
        this->value = value;
    }

    void setNext(Node* next) {
        this->next = next;
    }

    void setPrev(Node* prev) {
        this->prev = prev;
    }

    T getValue() const {
        return this->value;
    }

    Node* getNext() const {
        return this->next;
    }

    Node* getPrev() const {
        return this->prev;
    }
};

template <typename T>
class LinkedList {
private:
    Node<T>* head;
    Node<T>* tail;

public:
    LinkedList() {
        this->setHead(nullptr);
        this->setTail(nullptr);
    }

    ~LinkedList() {
        Node<T>* p = head;
        while (p != nullptr) {
            Node<T>* next = p->getNext();
            delete p;
            p = next;
        }
    }

    void setHead(Node<T>* head) {
        this->head = head;
    }

    void setTail(Node<T>* tail) {
        this->tail = tail;
    }

    void add(T value) {
        Node<T>* newNode = new Node<T>(value);

        newNode->setNext(nullptr);

        if (this->head == nullptr) {
            this->head = newNode;
            this->tail = newNode;

            newNode->setPrev(nullptr);

        } else {
            newNode->setPrev(this->tail);
            this->tail->setNext(newNode);

            this->tail = newNode;
        }
    }

    T remove() {
        if (this->head == nullptr) {
            throw std::out_of_range("List is empty");
        }

        T value = this->tail->getValue();

        if (this->head == this->tail) {
            delete this->head;
            this->head = nullptr;
            this->tail = nullptr;
        } else {
            tail = tail->getPrev();
            delete tail->getNext();
            tail->setNext(nullptr);
        }
    }

    void printState() const {

        Node<T>* p = head;
        while (p != nullptr) {
            std::cout << p->getValue() << "( << " << p << " ) -> ";
            p = p->getNext();
        }
        std::cout << std::endl;
    }


    T operator[](int index) {
        Node<T>* p = this->head;
        for (int i = 0; i < index; i++) {
            p = p->getNext();
        }
        return p->getValue();
    }

    int size() {
        int size = 0;
        Node<T>* p = head;
        while (p != nullptr) {
            size++;
            p = p->getNext();
        }
        return size;
    }

    void insert(int index, T value) {

        Node<T>* newNode = new Node<T>(value);
        Node<T>* p = head;

        for (int i = 0; i < index - 1; i++) {
            p = p->getNext();
        }

        newNode->setNext(p->getNext());
        newNode->setPrev(p);

        newNode->getNext()->setPrev(newNode);
        newNode->getPrev()->setNext(newNode);
    }

    T _delete(int index) {

        Node<T>* p = head;

        for (int i = 0; i < index; i++) {
            p = p->getNext();
        }

        p->getPrev()->setNext(p->getNext());
        p->getNext()->setPrev(p->getPrev());

        T value = p->getValue();
        delete p;

        return value;
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

    for(int i=0; i < list.size(); i++)
        std::cout << list[i] << " ";
    std::cout << std::endl;

    list._delete(2);

    list.printState();

    for(int i=0; i < list.size(); i++)
        std::cout << list[i] << " ";
    std::cout << std::endl;

    return 0;
}