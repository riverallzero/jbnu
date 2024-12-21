# DP, RGB 거리
# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 
# 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다. 

import sys

def minCost(mat):
    global N

    dp = [[0] * 3 for _ in range(N)]
    
    # dp[0] = mat[0]
    dp[0][0] = mat[0][0] # Red
    dp[0][1] = mat[0][1] # Green
    dp[0][2] = mat[0][2] # Blue
    
    for i in range(1, N):
        dp[i][0] = mat[i][0] + min(dp[i-1][1], dp[i-1][2])  # Red
        dp[i][1] = mat[i][1] + min(dp[i-1][0], dp[i-1][2])  # Green
        dp[i][2] = mat[i][2] + min(dp[i-1][0], dp[i-1][1])  # Blue
    
    return min(dp[N-1])

if __name__ == '__main__':
    # answer = 96
    # inputs = [
    #     '3\n',
    #     '26 40 83\n',
    #     '49 60 57\n',
    #     '13 89 99'
    # ]

    inputs = sys.stdin.readlines()

    N = int(inputs[0])

    mat = []
    for line in inputs[1:]:
        a, b, c = map(int, line.split())
        mat.append([a, b, c])

    print(minCost(mat))
