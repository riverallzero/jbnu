#include <iostream>
#include <cctype>

class Stack {
    char *array;
    int capacity;
    int top;

public:
    Stack(int capacity) : capacity(capacity), top(-1) {
        array = new char[capacity];
    }

    ~Stack() {
        delete[] array;
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

    int peek() {
        if (isEmpty()) {
            throw std::out_of_range("Stack underflow");
        }
        return array[top];
    }

    bool isEmpty() const {
        return top == -1;
    }

    void clear() {
        this->top = -1;
    }
};

int precedence(char op) { // 연산자 우선순위
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

std::string infixToPostfix(const std::string &infix) {
    std::string postfix;
    Stack stack(100);
    for (char c: infix) {
        if (isalpha(c) || isdigit(c)) {
            // 알파벳 또는 숫자는 그대로 추가
            postfix += c;
        } else if (c == '(') {
            stack.push(c);
        } else if (c == ')') { // 닫는 괄호 만날때까지 pop하고 추가
            while (!stack.isEmpty() && stack.peek() != '(') {
                postfix += stack.pop();
            }
            stack.pop(); // 스택에서 여는 괄호 제거
        } else { // 현재 연산자의 우선순위가 스택의 top에 있는 연산자의 우선순위보다 크거나 같을때까지 pop
            while (!stack.isEmpty() && precedence(c) <= precedence(stack.peek())) {
                postfix += stack.pop();
            }
            stack.push(c);
        }
    }
    while (!stack.isEmpty()) {
        postfix += stack.pop();
    }
    return postfix;
}

// 후위 계산식으로 계산 결과 추출
double evaluatePostfix(const std::string &postfix) {
    Stack stack(100);
    for (char c: postfix) {
        if (isdigit(c)) {
            stack.push(c - '0'); // 문자를 숫자로 변환해 저장
        } else {
            double val2 = stack.pop();
            double val1 = stack.pop();

            switch (c) {
                case '+':
                    stack.push(val1 + val2);
                    break;
                case '-':
                    stack.push(val1 - val2);
                    break;
                case '*':
                    stack.push(val1 * val2);
                    break;
                case '/':
                    stack.push(val1 / val2);
                    break;
            }
        }
    }
    return stack.pop(); // 최종 결과
}

int main() {
    std::string infix = "3*4+2*(3+2)";
    std::string postfix = infixToPostfix(infix);
    std::cout << "infix: " << infix << std::endl;
    std::cout << "postfix: " << postfix << std::endl;
    std::cout << "result -> " << evaluatePostfix(postfix) << std::endl;
    return 0;
}