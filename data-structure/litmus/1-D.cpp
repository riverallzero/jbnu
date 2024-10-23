// 문제) 정수 n을 입력받아 가로, 세로가 모두 n인 n x n 크기의 정사각형을 그리는 프로그램을 작성하시오. 
// 단, C++의 형식에 맞추어 cin과 cout을 이용해 입출력하셔야 합니다.

// INPUT
// 정사각형의 한 변의 길이를 나타내는 정수 n(1<=n<=100)을 입력 받습니다.

// OUTPUT
// 출력 형식은 Sample Output과 같은 형식을 따릅니다. 
// 사각형의 공간은 '*'로 표현합니다. 출력이 끝나면 개행처리 해줍니다.

#include <iostream>
 
class Square {
private:
    int size;
 
public:
    Square(int n) : size(n) {}
 
    void drawSquare() {
        for (int i = 0; i < size; ++i) {
            for (int j = 0; j < size; ++j) {
                std::cout << "*";
            }
            std::cout << std::endl;
        }
    }
};
 
int main() {
    int n;
    std::cin >> n;
 
    Square square(n);
 
    square.drawSquare();
 
    return 0;
}
