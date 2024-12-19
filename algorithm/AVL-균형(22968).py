# AVL Tree, 균형
# 양의 정수 V가 주어지면, 최대 V개의 정점을 사용해서 만들 수 있는 AVL Tree의 최대 높이를 출력하라

import sys

if __name__ == '__main__':
    inputs = sys.stdin.readlines()

    for line in inputs[1:]:
        v = int(line.strip())
        a = 1
        b = 2
        max_height = 0
        
        while a <= v:
            a, b = b, a + b + 1 # 피보나치 수열로 계산(수정) b = a + b -> b = a + b + 1
            max_height += 1
        print(max_height)
