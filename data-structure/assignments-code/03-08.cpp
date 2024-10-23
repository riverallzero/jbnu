#include <iostream>

class Node {
public:
    int data;
    Node* prev;
    Node* next;

    Node(int data) : data(data), prev(nullptr), next(nullptr) {

    }
};

class DoubleLinkedList {
public:
    Node* head;
    Node* tail;

    DoubleLinkedList() : head(nullptr), tail(nullptr) {

    }

    void add(int data) {
        Node* newNode = new Node(data);
        if(head == nullptr) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }

    void reverse() {
        Node* current = head;
        Node* temp = nullptr;

        while (current != nullptr) {
            temp = current->prev;
            current->prev = current->next;
            current->next = temp;
            current = current->prev;
        }

        temp = head;
        head = tail;
        tail = temp;
    }
};