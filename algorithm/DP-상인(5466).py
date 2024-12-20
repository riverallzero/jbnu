# DP, 상인
# 보트의 미터당 연료 비용, 상인이 사는 집의 위치, 각 시장이 열리는 날짜, 위치, 시장을 방문할 때 얻는 이익이 주어질 때 
# 여행을 끝마친 후 얻을 수 있는 최대 이익을 구하라

import sys
from collections import defaultdict

def segTree(arr, l, r):
    l += MAXN
    r += MAXN
    ans = -INF

    while l <= r:
        if l & 1: # l이 홀수인 경우 왼쪽 자식
            ans = max(ans, arr[l]) 
            l += 1 # 오른쪽 자식으로 이동
        if not r & 1: # r이 짝수인 경우 오른쪽 자식
            ans = max(ans, arr[r])
            r -= 1 # 왼쪽 자식으로 이동
        # 부모로 이동
        l //= 2
        r //= 2

    return ans

def update(arr, x, v):
    x += MAXN
    arr[x] = max(arr[x], v)
    while x > 1:
        x //= 2
        arr[x] = max(arr[x * 2], arr[x * 2 + 1])

def updateCost(x, v):
    update(uptree, x, v - u * x)
    update(downtree, x, v + d * x)

def findMax(a):
    return max(segTree(downtree, 0, a) - d * a, segTree(uptree, a, MAXN - 1) + u * a)

def processMarket(market):
    if not market:
        return 0
    
    market.sort()
    num_markets = len(market)
    U = [-INF] * num_markets
    D = [-INF] * num_markets

    # 시장 방문시 얻을 수 있는 최대 이익 계산
    for i in range(num_markets):
        temp = findMax(market[i][0])
        U[i] = temp
        D[i] = temp

    for i in range(num_markets):
        if i > 0:
            D[i] = max(D[i], D[i - 1] - d * (market[i][0] - market[i - 1][0]))
        D[i] += market[i][1]

    for i in range(num_markets - 1, -1, -1):
        if i < num_markets - 1:
            U[i] = max(U[i], U[i + 1] - u * (market[i + 1][0] - market[i][0]))
        U[i] += market[i][1]

    for i in range(num_markets):
        updateCost(market[i][0], max(U[i], D[i]))

if __name__ == '__main__':
    # answer = 50
    # inputs = [
    #     '4 5 3 100\n',
    #     '2 80 100\n',
    #     '20 125 130\n',
    #     '10 75 150\n',
    #     '5 120 110'
    # ]

    inputs = sys.stdin.readlines()

    n, u, d, s = map(int, inputs[0].split())

    MAXN = 500010 # 트리 크기
    INF = float('inf') 
    uptree = [-INF] * (2 * MAXN) # 올라가는 경로에 대한 트리
    downtree = [-INF] * (2 * MAXN) # 내려가는 경로에 대한 트리
    markets = defaultdict(list)

    for line in inputs[1:]:
        Tk, Lk, Mk = map(int, line.split())
        markets[Tk].append((Lk, Mk))

    # 집에서 출발할 때 0으로 초기화
    updateCost(s, 0)

    for i in range(1, MAXN):
        processMarket(markets[i])

    print(findMax(s))
    