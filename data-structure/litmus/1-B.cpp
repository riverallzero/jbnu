// 문제) 입력 되는 문자열에 대한 아래 요건을 만족하는 괄호 검사 프로그램을 만드시오.
// - 소괄호“()”, 중괄호“{}”, 대괄호“[]” 의 짝이 맞는지 확인
// - 큰 따옴표 사이에 대한 문자열 무시
// - 주석(한 줄 주석”//“, 여러줄 주석”/**/“)에 대한 무시 처리

// INPUT
// ”EOF“를 입력 받을 때까지 문자열을 입력

// OUTPUT
// 괄호 검사 성공 여부에 따라 출력문은 아래와 같고 오류 시 오류가 생긴 문장의 라인,문자까지만 인정
// 1) 성공 : OK, Line_count : (문장 수), bracket_count : (괄호 짝 수)
// 2) 오류 : Error, Line_count : (문장 수), bracket_count : (괄호 짝 수)

// - 아래 main 함수를 참조하여 checkMatching() 함수를 만드시오.
// int main(){
//     std::string Str,temp;
//     while(true){
//         std::getline(std::cin,temp);
//         if(temp=="EOF")break;
//         Str.append(temp);
//         Str.append("\n");
//         std::cin.clear();
//     }
//     checkMatching(Str);
//
//     return 0;
// }

#include <iostream>
#include <stdexcept>


class CheckMatch {
private:
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
                throw std::out_of_range("Stack Underflow");
            }
            return array[top];
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
public:
    void checkMatching(const std::string &inputString) {
        Stack dataStack(100);

        bool isInQuote = false; // '"'
        bool isInComment = false; // '//'
        bool isInBlockComment = false; // '/* */'
        int lineCount = 1;
        int bracketCount = 0;

        for (int i = 0; i < inputString.length() - 1; i++) { // EOF 직전의 '\n'은 제외 --> inputString.length() - 1
            char ch = inputString[i];

            if (ch == '\n') // '\n' 이면 무조건 줄 개수 카운트
                lineCount++;

            if (isInQuote) { // '"'가 시작 되다가 '"'가 나오면 따옴표가 끝난 것
                if (ch == '"') {
                    isInQuote = false;
                }

            } else if (isInComment) { // 주석이 시작 되다가 '\n'이 나오면 주석 해제
                if (ch == '\n') {
                    isInComment = false;
                }
            } else if (isInBlockComment) { // 여러줄 주석이 시작 되다가 '*/'이 나오면 주석 해제
                if (ch == '*' && i + 1 < inputString.length() && inputString[i + 1] == '/') {
                    isInBlockComment = false;
                    i++;
                }
            } else {
                if (ch == '"') { // 일단 '"'가 나오면 따옴표 시작이라고 가정
                    isInQuote = true;
                } else if (ch == '/' && i + 1 < inputString.length()) {
                    if (inputString[i + 1] == '/') { // '/'가 오고 바로 다음 '/'가 오면 주석 시작
                        isInComment = true;
                        i++;
                    } else if (inputString[i + 1] == '*') { // '/'가 오고 바로 다음 '*'가 오면 여러줄 주석 시작
                        isInBlockComment = true;
                        i++;
                    }
                } else {
                    switch (ch) {
                        case '(':
                        case '{':
                        case '[':
                            dataStack.push(ch);
                            break;
                        case ')':
                        case '}':
                        case ']':
                            if (dataStack.isEmpty() ||
                                (ch == ')' && dataStack.peek() != '(') ||
                                (ch == '}' && dataStack.peek() != '{') ||
                                (ch == ']' && dataStack.peek() != '[')) {
                                goto printError;
                            } else {
                                dataStack.pop();
                                bracketCount++;
                            }
                            break;
                    }
                }
            }
        }

        if (dataStack.isEmpty()) {
            std::cout << "OK, Line_count : " << lineCount << ", bracket_count : " << bracketCount << std::endl;
        } else {
            printError:
            std::cout << "Error, Line_count : " << lineCount << ", bracket_count : " << bracketCount << std::endl;
        }
    }
};


int main() {
    CheckMatch check;
    std::string Str, temp;
    while (true) {
        std::getline(std::cin, temp);
        if (temp == "EOF")
            break;
        Str.append(temp);
        Str.append("\n");
        std::cin.clear();
    }

    check.checkMatching(Str);

    return 0;
}
