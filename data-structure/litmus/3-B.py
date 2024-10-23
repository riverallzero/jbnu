'''원의 면적과 둘레
문제) 파이를 나타내는 PI=3.14를 전역 변수로 하여 원의 면적을 계산하는 함수 circleArea(radius)과 원의 둘레를 계산하는 함수 circleCircumference(radius)를 작성하고 테스트 하시오.  
- round 함수를 사용하여 소수 둘째 자리까지 표현하시오.

<INPUT>
2.2
 
<OUTPUT>
15.2
13.82'''

PI = 3.14

class Circle():
    global PI

    def circleArea(radius):
        return round(PI * (radius ** 2), 2)

    def circleCircumference(radius):
        return round(2 * PI * radius, 2)

def main():
    radius = float(input())

    print(Circle.circleArea(radius))
    print(Circle.circleCircumference(radius))


if __name__ == '__main__':
    main()