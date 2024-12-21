# DP, 123더하기 2
# 정수 n과 k가 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법 중에서 k번째로 오는 식을 구하라

import sys

n, k = map(int, sys.stdin.readline().rstrip().split()) # 4, 3
answers = set()

def DFS(value, answer):
    if value == n:
        answers.add(tuple(answer))
        return

    if value + 1 <= n:
        DFS(value + 1, answer + [1])

    if value + 2 <= n:
        DFS(value + 2, answer + [2])

    if value + 3 <= n:
        DFS(value + 3, answer + [3])

DFS(0, [])

if len(answers) < k: print(-1)
else:
    answers = list(answers)
    answers.sort()
    answer = answers[k-1]
    print(*answer, sep="+") # 1+2+1