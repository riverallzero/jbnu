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
