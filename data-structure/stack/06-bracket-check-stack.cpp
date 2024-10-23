#include <iostream>
#include <stdexcept>

class Stack {
    char* array;
    int capacity;
    int top;

public:
    Stack(int capacity) : capacity(capacity), top(-1) {
        array = new char[capacity]; // 초기 용량을 1로 설정하고 동적 할당
    }

    ~Stack() {
        delete[] array; // 동적 할당된 메모리 해제
    }

    void push(char item) {
        if (top + 1 == capacity) {
            throw std::out_of_range("Stack overflow");
        }
        array[++top] = item;
    }

    char pop() {
        if (isEmpty()) {
            throw std::out_of_range("Stack underflow");
        }
        return array[top--];
    }

    bool isEmpty() const {
        return top == -1;
    }

    int size() const {
        return top + 1;
    }

    void clear() {
        this->top = -1;
    }
};

bool isValid(Stack* stack, const std::string& s) {
    for (char c : s) {
        switch (c) {
            case '(': case '{': case '[':
                stack->push(c);
                break;
            case ')':
                if (stack->isEmpty() || stack->pop() != '(') return false;
                break;
            case '}':
                if (stack->isEmpty() || stack->pop() != '{') return false;
                break;
            case ']':
                if (stack->isEmpty() || stack->pop() != '[') return false;
                break;
        }
    }
    bool result = stack->isEmpty();
    stack->clear();

    return result;
}

int main() {
    
    Stack* stack = new Stack(100);
    
    std::cout << std::boolalpha;
    std::cout << isValid(stack, "()") << std::endl;       // true
    std::cout << isValid(stack, "()[]{}") << std::endl;   // true
    std::cout << isValid(stack, "(]") << std::endl;       // false
    std::cout << isValid(stack, "([)]") << std::endl;     // false
    std::cout << isValid(stack, "{[]}") << std::endl;     // true

    return 0;
}
