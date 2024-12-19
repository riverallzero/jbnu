# BFS & DFS, 특별한 오름
# 오름에서 선생님을 피해 찍을 수 있는 사진의 아름다움의 최댓값을 출력하라

import sys
from collections import deque

def maxY(N, teachers):
    que = deque([(0, 0, 0)])
    visited = set()

    def canGo(xx, yy):
        return yy >= 0 and xx + yy <= 2 * N and (xx, yy) not in teachers and (xx, yy) not in visited

    while que:
        x, y, h = que.popleft()

        if (x, y) == (2 * N, 0):            
            return h
        
        for dx, dy in [(x + 1, y + 1), (x + 1, y - 1)]:
            if canGo(dx, dy):
                que.append((dx, dy, max(h, dy)))
                visited.add((dx, dy))

    return -1

if __name__ == '__main__':
    # answer = 2
    # inputs = [
    #     '4 3\n',
    #     '2 2\n',
    #     '4 0\n',
    #     '5 3',
    # ]

    inputs = sys.stdin.readlines()

    N, M = map(int, inputs[0].split())
    teachers = set([(int(val.split()[0]), int(val.split()[1])) for val in inputs[1:]])
    print(maxY(N, teachers))
