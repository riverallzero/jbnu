#include <iostream>
#include <stdexcept>

class Stack {

private:
    int *array;
    int capacity;
    int top;
    int multiplier;


private:
    bool isFull() const {
        return top == capacity - 1;
    }

    bool isHalf() const {
        return top <= capacity / 2;
    }

    void increaseCapacity() {
        int newCapacity = capacity * this->multiplier;
        int *newArray = new int[newCapacity];

        for (int i=0; i<capacity; i++)
            newArray[i] = array[i];

        delete[] array;

        array = newArray;
        capacity = newCapacity;
    }

    void decreaseCapacity() {
        int newCapacity = capacity / 2 + 1;
        int *newArray = new int[newCapacity];

        for (int i=0; i < newCapacity; i++)
            newArray[i] = array[i];

        delete[] array;

        array = newArray;
        capacity = newCapacity;
    }


public:

    Stack(int capacity, int multiplier) : capacity(capacity), top(-1) {
        array = new int[capacity];
        this->multiplier = multiplier;
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
            throw std::out_of_range("Stack underflow");
        } else if (this->isHalf()) {
            this->decreaseCapacity();
        }
        return array[top--];
    }

    int peak() {
        if (isEmpty()) {
            throw std::out_of_range("Stack underflow");
        }
        return array[top];
    }

    int getSize() const {
        return top + 1;
    }

    int getCapacity() const {
        return capacity;
    }

    void display() {

        std::string out_str = "Stack ";
        out_str += "(capacity=" + std::to_string(this->getCapacity()) + " / ";
        out_str += "size=";
        out_str += std::to_string(this->getSize()) + ") || ";
        for(int i=0; i<top + 1; i++)
            out_str += std::to_string(array[i]) + " | ";
        out_str = out_str.substr(0, out_str.size() - 3);

        out_str.insert(0, 1, ' ');
        out_str.insert(0, 2, '|');
        out_str += " ||";


        for (int i=0; i<out_str.size(); i++)
            std::cout << "=";
        std::cout << std::endl;

        std::cout << out_str << std::endl;

        // cout "=" with length of out_str
        for (int i=0; i<out_str.size(); i++)
            std::cout << "=";
        std::cout << std::endl;
    }
};





int main(int argc, char *argv[])
{
    Stack stack(5, 3);

    for (int i=0; i < 10; i++) {
        stack.push(i * 10 + 10);
    }
    std::cout << stack.getCapacity() << std::endl; // 15가 출력되어야 함.


    for (int i=0; i < 10; i++) {
        stack.push(i * 10 + 10);
    }
    std::cout << stack.getCapacity() << std::endl; // 45가 출력되어야 함.


    return 0;
}
