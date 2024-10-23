// 문제) 게임에 참여하는 사람의 총 숫자는 N(≤5000)명이며, 이들은 원형으로 둥글게 모여 앉아 게임을 시작한다.
// 게임이 시작되면, 참여자 중 한 명이 숫자 K(≤5000)를 크게 외치며, 이 때부터 순서대로 K번째에 해당하는 사람이 일어나 게임에서 제외된다.
// 한 사람이 게임에서 제외될 때마다, 남은 참여자들은 다시 원형을 이루어 계속해서 같은 방식으로 K번째 사람을 찾아 게임에서 제외시킨다.
// 이러한 과정은 더 이상 제외시킬 사람이 없을 때, 즉 남은 사람이 없을 때까지 반복된다.
// 한 명당 D(≤100)개의 목숨을 갖고 시작하여, 위와 동일한 규칙대로 게임을 하되, 총 D번 걸려야 그제서야 게임에서 제외되도록 한다.
// 단, 맨 처음에는 1번부터 K만큼을 세게 되고, 걸린 사람이 죽었을 경우에는 바로 다음 사람부터 1을 세게 된다. 다만, 아직 게임에서 빠지지 않았을 경우, 걸린 사람부터 다시 1을 세게 된다.

// INPUT
// 7 1 2

// OUTPUT
// <1,2,3,4,5,6,7>

#include <iostream>
#include <stdexcept>

struct QueueItem {
    int value;
    int life;
};

class Queue {
private:
    QueueItem* array;
    int capacity;
    int ptr = -1;

public:
    Queue(int capacity) : capacity(capacity) {
        array = new QueueItem[capacity];
    }

    ~Queue() {
        delete[] array;
    }

    void printElements() const {
        for (int i = 0; i < ptr + 1; i++) {
            std::cout << array[i].value << "(" << array[i].life << ") ";
        }
        std::cout << std::endl;
    }

    bool isEmpty() const {
        return ptr == -1;
    }

    bool isFull() const {
        return ptr == capacity - 1;
    }

    void enqueue(int item, int life) {
        if (isFull()) {
            throw std::out_of_range("Queue overflow");
        }
        array[++ptr] = {item, life};
    }

    QueueItem dequeue() {
        if (isEmpty()) {
            throw std::out_of_range("Queue underflow");
        }

        QueueItem frontElement = array[0];

        for (int i = 0; i < ptr; i++) {
            array[i] = array[i + 1];
        }
        ptr--;

        return frontElement;
    }

    void findK(int k) {
        int count = 0;
        std::string result = "<";

        while (!isEmpty()) {
            QueueItem element = dequeue();

            if (count == k - 1) {
                element.life--;
                if (element.life > 0) {
                    enqueue(element.value, element.life);
                    count = 1;
                } else {
                    if (result.length() > 1) {
                        result += ",";
                    }
                    result += std::to_string(element.value);
                    count = 0;
                }
            } else {
                enqueue(element.value, element.life);
                count++;
            }
        }
        result += ">";
        std::cout << result << std::endl;
    }
};

int main() {
    int n;
    int k;
    int d;

    std::cin >> n >> k >> d;

    Queue queue(n);
    for (int i = 0; i < n; i++) {
        queue.enqueue(i + 1, d);
    }
//    queue.printElements();
    queue.findK(k);

    return 0;
}