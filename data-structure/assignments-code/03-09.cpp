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
    Node *head;
    Node *tail;

    DoubleLinkedList() : head(nullptr), tail(nullptr) {

    }

    int sumAroundNode(Node *node, int n) {
        if (node == nullptr) {
            return 0;
        }

        int sum = node->data;
        Node *temp = node->prev;
        int steps = n;

        while (temp != nullptr && steps > 0) {
            sum += temp->data;
            temp = temp->prev;
            steps--;
        }

        temp = node->next;
        steps = n;

        while (temp != nullptr && steps > 0) {
            sum += temp->data;
            temp = temp->next;
            steps--;
        }

        return sum;
    }
};