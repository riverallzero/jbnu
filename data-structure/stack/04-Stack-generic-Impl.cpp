#include <iostream>
#include <string>
#include <stdexcept>
#include <type_traits> // Include for std::is_same

template<typename T>
class Stack {
private:
    T *array;
    int capacity;
    int top;

public:
    Stack(int capacity) : capacity(capacity), top(-1) {
        array = new T[capacity];
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

    bool push(T item) {
        if (isFull()) {
            return false;
        }
        array[++top] = item;
        return true;
    }

    T pop() {
        if (isEmpty()) {
            throw std::out_of_range("Stack underflow");
        }
        return array[top--];
    }

    T peak() {
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
        for (int i = 0; i <= top; i++) {
            if constexpr (std::is_same_v<T, std::string>) {
                out_str += array[i]; // Directly append if T is std::string
            } else {
                out_str += std::to_string(array[i]); // Convert to string otherwise
            }
            if (i < top) {
                out_str += " | ";
            }
        }
        if (top >= 0) {
            out_str += " ||";
        }

        std::cout << std::string(out_str.size(), '=') << std::endl;
        std::cout << out_str << std::endl;
        std::cout << std::string(out_str.size(), '=') << std::endl;
    }
};





int main(int argc, char *argv[])
{
    Stack<int> stack(100);
    stack.display();

    stack.push(1);
    stack.push(2);
    stack.display();

    std::cout << "pop: " << stack.pop() << std::endl;
    std::cout << "pop: " << stack.pop() << std::endl;
    stack.display();

    Stack<std::string> stack2(100);

    stack2.push("abc");
    stack2.push("def");
    stack2.display();

    std::cout << "pop: " << stack2.pop() << std::endl;
    std::cout << "pop: " << stack2.pop() << std::endl;

    stack2.display();


    return 0;
}

