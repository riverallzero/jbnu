#include <iostream>
#include <stdexcept>

template <typename T>
class Queue {
private:
    T* array; // 요소를 저장할 동적 배열
    int capacity; // 배열의 최대 용량
    int frontIndex; // 큐의 앞부분 인덱스
    int rearIndex; // 큐의 뒷부분 인덱스

    // 용량이 가득 차면 2배로 늘림
    void resize() {
        int newCapacity = capacity * 2;
        T* newArray = new T[newCapacity];

        // 기존 요소를 새 배열로 복사
        for (int i = 0; i < this->size(); i++) {
            newArray[i] = array[(frontIndex + i) % capacity];
        }

        delete[] array;
        array = newArray;
        capacity = newCapacity;
        frontIndex = 0;
        rearIndex = this->size() -1;
    }

public:
    Queue(int initCapacity = 8) : capacity(initCapacity), frontIndex(0), rearIndex(-1) {
        array = new T[capacity];
    }

    ~Queue() {
        delete[] array;
    }

    void enqueque(const T& value) {
        if (this->size() == capacity) {
            resize();
        }
        rearIndex = (rearIndex + 1) % capacity;
        array[rearIndex] = value;
    }

    T dequeue() {
        if (isEmpty()) {
            throw std::out_of_range("Queue is empty");
        }

        T value = array[frontIndex++];
        return value;
    }

    T front() const {
        if (isEmpty()) {
            throw std::out_of_range("Queue is empty");
        }
        return array[frontIndex];
    }

    bool isEmpty() const {
        return this->size() == 0;
    }

    int size() const {
        return this->rearIndex - this->frontIndex + 1;
    }

    int getCapacity() const {
        return this->capacity;
    }

    void printElements() const {
        for (int i = 0; i < size(); i++) {
            std::cout << array[(frontIndex + i) % capacity] << " ";
        }
        std::cout << std::endl;
    }
};

int main() {
    Queue<int> q(1);

    // 삽입
    q.enqueque(1);
    std::cout << "Front: " << q.front() << " | Queue size: " << q.size() << " | Queue capacity: " << q.getCapacity() << std::endl;
    q.printElements();

    q.enqueque(2);
    std::cout << "Front: " << q.front() << " | Queue size: " << q.size() << " | Queue capacity: " << q.getCapacity()<< std::endl;
    q.printElements();

    q.enqueque(3);
    std::cout << "Front: " << q.front() << " | Queue size: " << q.size() << " | Queue capacity: " << q.getCapacity() << std::endl;
    q.printElements();


    // 삭제
    while (!q.isEmpty()) {
        std::cout << "Front: " << q.front() << " | Queue size: " << q.size() << " | Queue capacity: " << q.getCapacity() << std::endl;
        q.dequeue();
        q.printElements();

    }

    return 0;
}