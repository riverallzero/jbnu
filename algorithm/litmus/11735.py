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
    inputs = sys.stdin.readlines()

    V, E = map(int, inputs[0].strip().split()) # num of vertex, num of edge
    K = int(inputs[1].strip()) # start vertex

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
            