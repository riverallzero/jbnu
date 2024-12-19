# Greedy, 동전0
# 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다. 
# 동전을 적절히 사용해서 그 가치의 합을 K로 만드려고 한다. 
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

import sys

def ctrMin(K, datas):    
    datas.sort(reverse=True)
    ctr = 0

    for data in datas:
        ctr += K // data
        K %= data

    return ctr

if __name__ == '__main__':
    # answer = 6
    # inputs = [
    #     '10 4200\n',
    #     '1\n',
    #     '5\n',
    #     '10\n',
    #     '50\n',
    #     '100\n',
    #     '500\n',
    #     '1000\n',
    #     '5000\n',
    #     '10000\n',
    #     '50000'
    # ]

    inputs = sys.stdin.readlines()

    N, K = map(int, inputs[0].split())
    datas = list(map(int, inputs[1:]))

    print(ctrMin(K, datas))