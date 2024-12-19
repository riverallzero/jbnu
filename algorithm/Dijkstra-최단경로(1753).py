# Dijkstra, 최단경로
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하라

import heapq
import sys

def findMin(graph, start):
    costs = [float('inf') for _ in range(V)]
    costs[start-1] = 0

    que = [(0, start)]

    while que:
        curr_cost, curr_vertex = heapq.heappop(que)

        if curr_cost > costs[curr_vertex-1]:
            continue

        for neighbor, weight in graph[curr_vertex]:
            cost = curr_cost + weight

            if cost < costs[neighbor-1]:
                costs[neighbor - 1] = cost
                heapq.heappush(que, (cost, neighbor))

    return costs

if __name__ == '__main__':
    # answer = 0 \n 2 \n 3 \n 7 \n INF
    # inputs = [
    #     '5 6\n',
    #     '1\n',
    #     '5 1 1\n',
    #     '1 2 2\n',
    #     '1 3 3\n',
    #     '2 3 4\n',
    #     '2 4 5\n',
    #     '3 4 6'
    # ]

    inputs = sys.stdin.readlines()

    V, E = map(int, inputs[0].strip().split()) 
    K = int(inputs[1].strip())

    graph = {i + 1: [] for i in range(V)}

    for line in inputs[2:]:
        u, v, w = map(int, line.strip().split())

        graph[u].append((v,w))

    result_table = findMin(graph, K)

    for result in result_table:
        if result == float('inf'):
            print('INF')
        else:
            print(result)
            