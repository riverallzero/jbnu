#include <iostream>
#include <stdexcept>

class Stack {

private:
    int *array;
    int capacity;
    int top;

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

    bool isFull() const {
        return top == capacity - 1;
    }

    bool push(int item) {
        if (isFull()) {
            // 가득 차면 무언가 해야함
            return false;
        }
        array[++top] = item;
        return true;
    }

    int pop() {
        if (isEmpty()) {
            // 비어있으면 무언가 해야함
            throw std::out_of_range("Stack underflow");
        }
        return array[top--];
    }

    int peak() {
        if (isEmpty()) {
            throw std::out_of_range("Stack underflow");
        }
        return array[top];
    }

    int size() const {
        return top + 1;
    }

    void display() {

        std::string out_str = "Stack (size=";
        out_str += std::to_string(top + 1) + ") || ";
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
    Stack stack(5);
    stack.display();

    int value = 1;
    while(!stack.isFull()){
        stack.push(value++ * 10);
        stack.display();
    }

    return 0;
}
