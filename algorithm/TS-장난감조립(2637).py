# Tology Sorting, 장난감 조립
# 하나의 완제품을 조립하는데 필요한 기본 부품의 수를 한 줄에 하나씩 출력하되(중간 부품은 출력하지 않음), 
# 반드시 기본 부품의 번호가 작은 것부터 큰 순서가 되도록 한다. 
# 각 줄에는 기본 부품의 번호와 소요 개수를 출력한다.

import sys
from collections import defaultdict, deque

def solve(N, arr):
    graph = defaultdict(list)  # 그래프: X -> (Y, K)
    basic_part = [i for i in range(1, N + 1)] # 기본 부품

    degree_arr = [0] * (N + 1)  # 진입 차수
    for x, y, k in arr:
        graph[y].append((x, k))
        degree_arr[x] += 1

        if x in basic_part:
            basic_part.remove(x)

    needs = [[0] * (N + 1) for _ in range(N + 1)]  # 각 부품별 필요 기본 부품 수

    # 진입 차수가 0인 노드부터 시작
    que = deque()
    for i in range(1, N + 1):
        if degree_arr[i] == 0:
            que.append(i)

    while que:
        curr = que.popleft()

        # 현재 부품이 기본 부품인 경우
        for next_part, count in sorted(graph[curr]):
            if curr in basic_part:  # 기본 부품
                needs[next_part][curr] += count
            else:  # 중간 부품
                for i in range(1, N + 1):
                    needs[next_part][i] += needs[curr][i] * count

            # 진입 차수 감소 및 큐에 추가
            degree_arr[next_part] -= 1
            if degree_arr[next_part] == 0:
                que.append(next_part)

    # 완제품(N)을 만드는 데 필요한 기본 부품만 출력
    for i in range(1, N):
        if needs[N][i] > 0:
            print(f'{i} {needs[N][i]}')
    
if __name__ == '__main__':
    # answer = [
    #     1 16
    #     2 16
    #     3 9
    #     4 17
    # ]
    # inputs = [
    #     '7\n',
    #     '8\n',
    #     '5 1 2\n',
    #     '5 2 2\n',
    #     '7 5 2\n',
    #     '6 5 2\n',
    #     '6 3 3\n',
    #     '6 4 4\n',
    #     '7 6 3\n',
    #     '7 4 5'
    # ]

    inputs = sys.stdin.readlines()

    N = int(inputs[0])  
    M = int(inputs[1])  
    arr = [tuple(map(int, line.split())) for line in inputs[2:]]

    solve(N, arr)
