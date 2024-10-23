#include <iostream>
#include <stdexcept>

class Stack {
private:
    int* array;
    int capacity;
    int top;

private:
    bool isFull() const {
        return top == capacity - 1;
    }

    bool isHalf() const {
        return top <= capacity / 2;
    }

    void increaseCapacity() {
        int newCapacity = capacity * 2;
        int *newArray = new int[newCapacity];

        for (int i = 0; i < capacity; i++)
            newArray[i] = array[i];

        delete[] array;

        array = newArray;
        capacity = newCapacity;
    }

    void decreaseCapacity() {
        int newCapacity = capacity / 2 + 1;
        int *newArray = new int[newCapacity];

        for (int i = 0; i < newCapacity; i++)
            newArray[i] = array[i];

        delete[] array;

        array = newArray;
        capacity = newCapacity;
    }

public:
    Stack(int capacity) : capacity(capacity), top(-1) {
        array = new int[capacity];
    }

    ~Stack() {
        delete[] array;
    }

    bool isEmpty() const {
        return top == -1;
    }

    void push(int item) {
        if (this->isFull()) {
            this->increaseCapacity();
        }
        array[++top] = item;
    }

    int pop() {
        if (this->isEmpty()) {
            throw std::out_of_range("Stack Underflow");
        } else if (this->isHalf()) {
            this->decreaseCapacity();
        }
        return array[top--];
    }

    int peek() {
        if (isEmpty()) {
            throw std::out_of_range("Stack Underflow");
        }
        return array[top];
    }

    int getSize() const {
        return top + 1;
    }

    int getCapacity() const {
        return capacity;
    }

    bool contains(int item) const {
        int topIndex = top;

        while (topIndex >= 0) {
            if (array[topIndex] == item) {
                return true;
            }
            topIndex--;
        }
        return false;
    }
};


int main() {
    Stack stack(10);

    for (int i = 1; i < 11; i++) {
        stack.push(i);
    }

    std::cout << std::boolalpha;
    std::cout << stack.contains(3) << std::endl;
}
