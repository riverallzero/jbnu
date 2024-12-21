# DC, 종이의 개수
# 1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# 2. (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력하라

import sys

def findCtr(N, arr):
    val_ctr = {'-1': 0, '0': 0, '1': 0}

    def splitFind(a, b, c, d):
        init_val = arr[a][c]
        is_same = True

        for i in range(a, b):
            for j in range(c, d):
                if arr[i][j] != init_val:
                    is_same = False
                    break
            if not is_same:
                break

        if is_same:
            val_ctr[str(init_val)] += 1
        else:
            n = (b - a) // 3  
            for i in range(3): 
                for j in range(3):
                    splitFind(a + i * n, a + (i + 1) * n, c + j * n, c + (j + 1) * n)

    splitFind(0, N, 0, N)

    return val_ctr

if __name__ == '__main__':
    # answer
    #     10
    #     12
    #     11 
    # inputs = [
    #     '9\n',
    #     '0 0 0 1 1 1 -1 -1 -1\n',
    #     '0 0 0 1 1 1 -1 -1 -1\n',
    #     '0 0 0 1 1 1 -1 -1 -1\n',
    #     '1 1 1 0 0 0 0 0 0\n',
    #     '1 1 1 0 0 0 0 0 0\n',
    #     '1 1 1 0 0 0 0 0 0\n',
    #     '0 1 -1 0 1 -1 0 1 -1\n',
    #     '0 -1 1 0 1 -1 0 1 -1\n',
    #     '0 1 -1 1 0 -1 0 1 -1',
    # ]

    inputs = sys.stdin.readlines()

    N = int(inputs[0])
    arr = [val.split() for val in inputs[1:]]

    results = findCtr(N, arr)
    for result in results.values():
        print(result)