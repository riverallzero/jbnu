import sys

def findPath(N, arr):
    INF = float('inf')
    mintime_arr = [INF] * (N + 1)
    mintime_arr[1] = 0
    
    # N-1번 반복하여 최단 거리 갱신
    for i in range(N-1):
        updated = False
        for A, B, C in arr:
            # 현재 노드까지의 비용이 유효하고, 현재 노드를 거쳐 가는 것이 더 저렴한 경우 -> 최단 거리 갱신
            if mintime_arr[A] != INF and mintime_arr[A] + C < mintime_arr[B]:
                mintime_arr[B] = mintime_arr[A] + C
                updated = True
        if not updated:
            break
    
    # 음수 사이클 검출
    has_cycle = [False] * (N + 1)
    for A, B, C in arr:
        # 갱신 가능한 경우 -> 사이클 존재
        if mintime_arr[A] != INF and mintime_arr[A] + C < mintime_arr[B]:
            has_cycle[B] = True
            
    # 음수 사이클의 영향을 받는 모든 정점 표시
    for i in range(N):
        for A, B, C in arr:
            if has_cycle[A]:
                has_cycle[B] = True
    
    # 음수 사이클 존재하는 경우 -> -1 출력
    if any(has_cycle[2:]):
        print(-1)
        return
    
    # 음수 사이클이 없는 경우 -> 최단 거리 출력
    for i in range(2, N + 1):
        if mintime_arr[i] == INF:
            print(-1)
        else:
            print(mintime_arr[i])

if __name__ == '__main__':
    # answer = 4 \n 3
    # inputs = [
    #     '3 4\n',
    #     '1 2 4\n',
    #     '1 3 3\n',
    #     '2 3 -1\n',
    #     '3 1 -2'
    # ]

    inputs = sys.stdin.readlines()
    N, M = map(int, inputs[0].split())
    arr = [tuple(map(int, line.split())) for line in inputs[1:]]

    findPath(N, arr)
