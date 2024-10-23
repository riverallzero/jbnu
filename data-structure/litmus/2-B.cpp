// 문제) 두 수를 입력 받아 두 수의 덧셈, 뺄셈, 곰셉, 나눗셈을 하는 프로그램을 작성하시오.

// INPUT
// 두 수를 입력 받는다.
// 두 번째 수에는 0이 들어가지 않는다.

// OUTPUT
// 두 수의 덧셈, 뺄셈, 곱셈, 나눗셈을 한 값을 출력한다.
// 출력 값은 모두 정수형이다.

#include <iostream>

class Calculate {
private:
    int a;
    int b;

public:
    Calculate(int a, int b) : a(a), b(b) {}
    ~Calculate() {}

    void fourOperation() {
        std::cout << a + b << " " << a - b << " " << a * b << " " << a / b << std::endl;
    }
};

int main() {
    int a;
    int b;
    std::cin >> a >> b;

    Calculate calculate(a, b);

    calculate.fourOperation();

    return 0;
}