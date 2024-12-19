# Greedy, ATM
# 줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때,
# 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하라

import sys

def minTime(arr):
    arr.sort()
    
    dp = [0] * N

    dp[0] = arr[0]
    
    for i in range(1, N):
        dp[i] = dp[i-1]+arr[i]

    return sum(dp)

if __name__ == '__main__':
    # answer = 32
    # inputs = [
    #     '5\n',
    #     '3 1 4 3 2'
    # ]

    inputs = sys.stdin.readlines()

    N = int(inputs[0])
    P_arr = [int(val) for val in inputs[1].split()]
    print(minTime(P_arr))
