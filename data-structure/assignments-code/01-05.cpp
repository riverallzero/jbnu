#include <iostream>
#include <stdexcept>

template<typename T>
class Stack {
private:
    T* array;
    int capacity;
    int top;
    int multiplier;

    static_assert(std::is_same<T, int>::value, "Type error");

private:
    bool isFull() const {
        return top == capacity - 1;
    }

    bool isMul() const {
        return top <= capacity / this -> multiplier;
    }

    void increaseCapacity() {
        int newCapacity = capacity * this -> multiplier;
        int *newArray = new int[newCapacity];

        for (int i = 0; i < capacity; i++)
            newArray[i] = array[i];

        delete[] array;

        array = newArray;
        capacity = newCapacity;
    }

    void decreaseCapacity() {
        int newCapacity = capacity / this -> multiplier;
        int *newArray = new int[newCapacity];

        for (int i = 0; i < newCapacity; i++)
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

    void push(T item) {
        if (this -> isFull()) {
            this -> increaseCapacity();
        }
        array[++top] = item;
    }

    T pop() {
        if (this -> isEmpty()) {
            throw std::out_of_range("Stack Underflow");
        } else if (this -> isMul()) {
            this -> decreaseCapacity();
        }
        return array[top--];
    }

    int getCapacity() const {
        return capacity;
    }
};


int main(int argc, char* argv[]) {
    Stack<int> stack(5, 3); // capacity=5, multiplier=3

    for (int i = 0; i < 10; i++){
        stack.push(i);
    }

    std::cout << stack.getCapacity() << std::endl; // 15

    for (int i = 0; i < 10; i++)
        stack.push(i + 10);

    std::cout << stack.getCapacity() << std::endl; // 45
}
