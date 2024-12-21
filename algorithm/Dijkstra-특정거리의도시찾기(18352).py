# Dijkstra, 특정 거리의 도시 찾기
# 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 
# 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하라
# X로부터 출발하여 도달할 수 있는 도시 중에서, 
# 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
# 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.

import sys
import heapq

def findCity(graph, start, N):
    costs = [float('inf') for _ in range(N)]

    costs[start-1] = 0

    que = [(0, start)]
    
    while que:
        curr_cost, curr_vertex = heapq.heappop(que)

        if curr_cost > costs[curr_vertex-1]:
            continue
        
        if curr_vertex in graph:
            for neighbor, weight in graph[curr_vertex]:
                cost = curr_cost + weight

                if cost < costs[neighbor-1]:
                    costs[neighbor-1] = cost
                    heapq.heappush(que, (cost, neighbor))

    return costs

if __name__ == '__main__':    
    # answer = 4
    # inputs = [
    #     '4 4 2 1\n',
    #     '1 2\n',
    #     '1 3\n',
    #     '2 3\n',
    #     '2 4'
    # ]

    inputs = sys.stdin.readlines()

    N, M, K, X = map(int, inputs[0].strip().split())

    graph = {i+1: [] for i in range(N)}

    for line in inputs[1:]:
        try:
            u, v = map(int, line.strip().split())
        except:
            continue

        graph[u].append((v,1))

    result_table = findCity(graph, X, N)        
    results = sorted([v + 1 for v, val in enumerate(result_table) if val == K])

    if len(results) == 0:
        print(-1)

    else:
        for result in results:
            print(result)
