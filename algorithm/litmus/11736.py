import sys
import heapq

def findCity(graph, start):
    costs = [float('inf') for _ in range(N)]

    costs[start-1] = 0

    que = [(0, start)]
    
    while que:
        curr_cost, curr_vertex = heapq.heappop(que)

        if curr_cost > costs[curr_vertex-1]:
            continue
        
        for neighbor, weight in graph[curr_vertex]:
            cost = curr_cost + weight

            if cost < costs[neighbor-1]:
                costs[neighbor-1] = cost
                heapq.heappush(que, (cost, neighbor))

    return costs

if __name__ == '__main__':    
    inputs = sys.stdin.readlines()

    # N: num of city, M: num of load, K: target cost, X: start vertex
    N, M, K, X = map(int, inputs[0].strip().split())

    graph = {i+1: [] for i in range(N)}

    for line in inputs[1:]:
        u, v = map(int, line.strip().split())

        graph[u].append((v,1))

    result_table = findCity(graph, X)
    results = [v+1 if val == K else None for v, val in enumerate(result_table)]

    if all(val is None for val in results):
        print(-1)
    for result in results:
        if result is not None:
            print(result)
