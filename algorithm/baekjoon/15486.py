import sys

def findMax(N, T, P):
    dp = [0 for _ in range(N + 1)]

    for i in range(N - 1, -1, -1):
        if i + T[i] <= N:
            dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])
        else:
            dp[i] = dp[i+1]

    return dp[0]

if __name__ == '__main__':
    # answer = 45
    # inputs = [
    #     '7\n',
    #     '3 10\n',
    #     '5 20\n',
    #     '1 10\n',
    #     '1 20\n',
    #     '2 15\n',
    #     '4 40\n',
    #     '2 200'
    # ]

    inputs = sys.stdin.readlines()

    N = int(inputs[0])

    T, P = [], []
    for n in range(1, N+1):
        T.append(int(inputs[n].split()[0]))
        P.append(int(inputs[n].split()[1]))
        
    print(findMax(N, T, P))
