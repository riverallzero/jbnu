#include <iostream>

class DataStructure {
protected:
    int *array;
    int capacity;
    int ptr = -1;

protected:
    void increaseCapacity() {
        int newCapacity = capacity * 2;
        int *newArray = new int[newCapacity];

        for (int i = 0; i < capacity; i++) {
            newArray[i] = array[i];
        }

        delete[] array;
        array = newArray;
        capacity = newCapacity;
    }

    void decreaseCapacity() {
        int newCapacity = capacity / 2 + 1;
        int *newArray = new int[newCapacity];

        for (int i = 0; i < newCapacity; i++) {
            newArray[i] = array[i];
        }

        delete[] array;
        array = newArray;
        capacity = newCapacity;
    }

public:
    explicit DataStructure(int capacity) : capacity(capacity) {
        array = new int[capacity];
    }

    ~DataStructure() {
        delete[] array;
    }

    virtual void printElements() const {
        throw std::runtime_error("Not implemented");
    }

    virtual bool isEmpty() const {
        throw std::runtime_error("Not implemented");
    }

    virtual bool isFull() const {
        throw std::runtime_error("Not implemented");
    }

    virtual void add(int item) {
        throw std::runtime_error("Not implemented");
    }

    virtual int remove() {
        throw std::runtime_error("Not implemented");
    }

    virtual int size() {
        throw std::runtime_error("Not implemented");
    }
};

class Stack : public DataStructure {
public:
    Stack(int capacity) : DataStructure(capacity) {
    }

    ~Stack() {
    }

    void printElements() const override {
        for (int i = 0; i < ptr + 1; i++) {
            std::cout << array[i] << " ";
        }
        std::cout << std::endl;
    }

    bool isEmpty() const override {
        return ptr == -1;
    }

    bool isFull() const override {
        return ptr == capacity - 1;
    }

    void add(int item) override {
        if (isFull()) {
            increaseCapacity();
        }
        array[++ptr] = item;
    }

    int remove() override {
        if (isEmpty()) {
            throw std::out_of_range("Stack underflow");
        } else if (ptr <= capacity / 2) {
            decreaseCapacity();
        }

        return array[ptr--];
    }

    int size() override {
        return ptr + 1;
    }
};

class Queue : public DataStructure {
public:
    Queue(int capacity) : DataStructure(capacity) {
    }

    ~Queue() {
    }

    void printElements() const override {
        for (int i = 0; i < ptr + 1; i++) {
            std::cout << array[i] << " ";
        }
        std::cout << std::endl;
    }

    bool isEmpty() const override {
        return ptr == -1;
    }

    bool isFull() const override {
        return ptr == capacity - 1;
    }

    void add(int item) override {
        if (isFull()) {
            increaseCapacity();
        }
        array[++ptr] = item;
    }

    int remove() override {
        if (isEmpty()) {
            throw std::out_of_range("Queue underflow");
        } else if (ptr <= capacity / 2) {
            decreaseCapacity();
        }

        // Queue는 맨 앞 요소를 먼저 제거하므로 왼쪽으로 한칸씩 이동
        int frontElement = array[0];

        for (int i = 0; i < ptr; i++) {
            array[i] = array[i + 1];
        }
        ptr--;

        return frontElement;
    }

    int size() override {
        return ptr + 1;
    }
};

int main() {
    // Stack
    std::cout << "STACK=====================" << std::endl;
    Stack stack(4);

    for (int i = 0; i < 10; i++) {
        stack.add(i + 10);
    }
    std::cout << "Size: " << stack.size() << std::endl;
    stack.printElements();

    for (int i = 0; i < 6; i++) {
        stack.remove();
    }
    std::cout << "Size: " << stack.size() << std::endl;
    stack.printElements();

    // Queue
    std::cout << "\nQUEUE=====================" << std::endl;
    Queue queue(4);

    for (int i = 0; i < 10; i++) {
        queue.add(i + 10);
    }
    std::cout << "Size: " << queue.size() << std::endl;
    queue.printElements();

    for (int i = 0; i < 6; i++) {
        queue.remove();
    }
    std::cout << "Size: " << queue.size() << std::endl;
    queue.printElements();

    return 0;
}