# DP, 상인
# 보트의 미터당 연료 비용, 상인이 사는 집의 위치, 각 시장이 열리는 날짜, 위치, 시장을 방문할 때 얻는 이익이 주어질 때 
# 여행을 끝마친 후 얻을 수 있는 최대 이익을 구하라

import sys

def segmentTree(arr, l, r):
    ans = INF

    # 트리 인덱스 초기화
    l += MAXN
    r += MAXN

    while l <= r:
        if l & 1: # l이 홀수인 경우 왼쪽 자식
            ans = max(ans, arr[l]) # 최대값 갱신
            l += 1 # l을 오른쪽 자식으로 이동
        if not (r & 1): # r이 짝수인 경우 오른쪽 자식
            ans = max(ans, arr[r]) # 최대값 갱신
            r -= 1 # r을 왼쪽 자식으로 이동
        l >>= 1 # l을 부모로 이동
        r >>= 1 # r을 부모로 이동

    return ans

def update(arr, x, v):
    x += MAXN # 인덱스를 트리 중간으로 설정
    arr[x] = max(arr[x], v) # 현재 위치에 최대값 저장

    while x > 1:
        arr[x >> 1] = max(arr[x], arr[x ^ 1]) # 부모 노드 갱신
        x >>= 1 # x를 부모로 이동

def updateCost(x, v):
    update(uptree, x, v - U * x) # 올라갈때 연료 비용 업데이트
    update(downtree, x, v + D * x) # 내려갈때 연료 비용 업데이트

def findMax(a): # uptree와 downtree를 비교해 최대값 도출
    return max(segmentTree(downtree, 0, a) - D * a, segmentTree(uptree, a, MAXN - 1) + U * a)

def processMarket(market):
    if not market:
        return

    market.sort() # Tk(시장이 열리는 날짜) 순으로 정렬
    num_markets = len(market)
    U_arr, D_arr = [0] * num_markets, [0] * num_markets

    # 시장 방문시 얻을 수 있는 최대 이익 계산
    for i in range(num_markets):
        temp = findMax(market[i][0])
        U_arr[i] = temp
        D_arr[i] = temp

    # 내려갈 때 이익 계산
    for i in range(1, num_markets):
        D_arr[i] = max(D_arr[i], D_arr[i - 1] - D * (market[i][0] - market[i - 1][0]))

    # 올라갈 때 이익 계산
    for i in range(num_markets - 2, -1, -1):
        U_arr[i] = max(U_arr[i], U_arr[i + 1] - U * (market[i + 1][0] - market[i][0]))

    # 올라갈 때, 내려갈 때 이익 합산
    for i in range(num_markets):
        D_arr[i] += market[i][1]
        U_arr[i] += market[i][1]

    # 올라갈 때, 내려갈 때를 모두 고려한 최대 이익 계산
    for i in range(num_markets):
        updateCost(market[i][0], max(U_arr[i], D_arr[i]))

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

    N, U, D, S = map(int, inputs[0].split())

    MAXN = 543210 # 트리 크기
    INF = float('-inf') # 최솟값을 찾기 위한 음의 무한대
    uptree = [INF] * (2 * MAXN) # 올라가는 경로에 대한 트리
    downtree = [INF] * (2 * MAXN) # 내려가는 경로에 대한 트리
    markets = [[] for _ in range(MAXN)] # 시장 위치 정보

    for line in inputs[1:]:
        Tk, Lk, Mk = map(int, line.split())
        markets[Tk].append((Lk, Mk))

    # 집에서 출발할 때 0으로 초기화
    updateCost(S, 0)
    for i in range(1, 500002):
        processMarket(markets[i])

    print(findMax(S))
