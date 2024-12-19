import sys
from collections import defaultdict, deque

def makeLine(arr):
    adj_list = defaultdict(list)
    degree_arr = [0] * (N + 1)

    # 진입 차수, 인접 리스트 생성
    for in_val, out_val in arr:
        adj_list[in_val].append(out_val)
        degree_arr[out_val] += 1

    # 큐에 진입 차수 0인 노드 추가
    que = deque()
    for v in range(1, N + 1):
        if degree_arr[v] == 0:
            que.append(v)

    result = []
    while que:
        curr_val = que.popleft() # 오름차순으로 처리
        result.append(curr_val)

        # 현재 노드와 연결된 간선 제거
        for out_val in sorted(adj_list[curr_val]):
            degree_arr[out_val] -= 1
            # 진입 차수가 0이면 큐에 추가
            if degree_arr[out_val] == 0:
                que.append(out_val)

    return ' '.join(map(str, result))

if __name__ == '__main__':
    # answer = 3 1 4 2
    # inputs = [
    #     '4 2\n',
    #     '4 2\n',
    #     '3 1'
    # ]

    inputs = sys.stdin.readlines()

    N, M = map(int, inputs[0].split())
    arr = [(int(val.split()[0]), int(val.split()[1])) for val in inputs[1:]]

    print(makeLine(arr))
