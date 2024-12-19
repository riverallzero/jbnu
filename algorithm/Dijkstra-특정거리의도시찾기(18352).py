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
