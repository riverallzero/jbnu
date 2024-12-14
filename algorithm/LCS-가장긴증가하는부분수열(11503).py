import sys

def find(i):
    # 이미 계산된 값은 반환
    if dp[i] != -1:
        return dp[i]

    # 최소값은 자기 자신인 경우 -> 1
    dp[i] = 1

    # A[i]를 끝으로 하는 부분 수열을 찾음
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], find(j) + 1)

    return dp[i]

if __name__ == '__main__':
    # answer = 6
    # inputs = [
    #     '6\n',
    #     '10 20 10 30 20 50'
    # ]

    inputs = sys.stdin.readlines()

    N = int(inputs[0])
    A = list(map(int, inputs[1].split()))

    dp = [-1] * N

    # 모든 i에 대해 LIS 계산 -> 최대값 출력
    ctr = 0
    for i in range(N):
        ctr = max(ctr, find(i))
    print(ctr)
