// 문제) 중위 수식을 입력받아 후위 수식 표기로 변환해 계산하고 결과를 출력하는 프로그램을 작성하라.

// INPUT
// - 입력 수식에 사용되는 모든 숫자는 실수 범위로 주어지며, 연산자는 +,-,*,/ 이다. 주어지는 술식에는 괄호가 포함된다. 
// - 0으로 나누려하는 경우 "Error : zero division error"를 출력하고, 아를 제외하고 주어진 수식에 오류는 없다고 가정한다.

// OUTPUT
// 결과는 실수형(double)으로 소수 둘째자리로 출력 

#include <iostream>
#include <cstring>
#include <cctype>
#include <string>
#include <stdexcept>
#include <sstream>
#include <iomanip>

class Stack {
    double* array;
    int capacity;
    int top;

public:
    Stack(int capacity) : capacity(capacity), top(-1) {
        array = new double[capacity];
    }

    ~Stack() {
        delete[] array;
    }

    void push(double item) {
        if (top + 1 == capacity) {
            double* newArray = new double[capacity * 2];
            memcpy(newArray, array, capacity * sizeof(double));
            delete[] array;
            array = newArray;
            capacity *= 2;
        }
        array[++top] = item;
    }

    double pop() {
        if (isEmpty()) {
            throw std::out_of_range("Stack underflow");
        }
        return array[top--];
    }

    bool isEmpty() const {
        return top == -1;
    }

    double peek() const {
        if (isEmpty()) {
            throw std::out_of_range("Stack is empty");
        }
        return array[top];
    }

    void clear() {
        top = -1;
    }
};

int precedence(char op) {
    if (op == '(' || op == ')') return 0;
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return -1;
}

std::string infixToPostfix(const std::string& infix) {
    std::string postfix;
    Stack stack(100);

    for (size_t i = 0; i < infix.size(); i++) {
        char c = infix[i];

        if (isdigit(c) || c == '.') { // 숫자와 소수점 구분
            postfix += c; // 실수를 만들기 위해 추가
            if (i + 1 == infix.size() || !isdigit(infix[i + 1]) && infix[i + 1] != '.') { // 실수에서 마지막 숫자인지 확인
                postfix += ' '; // 공백으로 숫자 구분
            }
        } else if (c == '(') {
            stack.push(c);
        } else if (c == ')') {
            while (!stack.isEmpty() && static_cast<char>(stack.peek()) != '(') {
                postfix += static_cast<char>(stack.pop());
                postfix += ' ';
            }
            stack.pop();
        } else if (precedence(c) > 0) {
            while (!stack.isEmpty() && precedence(c) <= precedence(static_cast<char>(stack.peek()))) {
                postfix += static_cast<char>(stack.pop());
                postfix += ' ';
            }
            stack.push(c);
        }
    }

    while (!stack.isEmpty()) {
        postfix += static_cast<char>(stack.pop());
        postfix += ' ';
    }

    return postfix;
}

double evaluatePostfix(const std::string& postfix) {
    Stack stack(100);
    std::istringstream tokens(postfix);
    std::string token;

    while (tokens >> token) { // '>>' 으로 입력된 문자열에서 공백으로 숫자들을 구분
        if (isdigit(token[0]) || (token.size() > 1 && token[1] == '.')) { // 구분된 숫자를 double 타입으로 stod()를 이용해 스택에 올림
            stack.push(stod(token));
        } else {
            double val2 = stack.pop();
            double val1 = stack.pop();
            switch (token[0]) {
                case '+': stack.push(val1 + val2); break;
                case '-': stack.push(val1 - val2); break;
                case '*': stack.push(val1 * val2); break;
                case '/':
                    if (val2 == 0) throw std::runtime_error("Error : zero division error");
                    stack.push(val1 / val2);
                    break;
            }
        }
    }
    return stack.pop();
}

int main() {
    std::string infix;
    std::getline(std::cin, infix);

    try {
        std::string postfix = infixToPostfix(infix);
        std::cout << std::fixed << std::setprecision(2) <<  evaluatePostfix(postfix) << std::endl;
    } catch (const std::exception& e) {
        std::cout << e.what() << std::endl;
    }

    return 0;
}
