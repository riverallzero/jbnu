def counter(x):
    counts = 0
    for i in range(1, N + 1):
        counts += min(x // i, N)

    return counts

def findK(N, K):
    left, right = 1, N * N

    while left < right:
        mid = (left + right) // 2
        
        if counter(mid) >= K:
            right = mid
        else:
            left = mid + 1
    
    return left

if __name__ == '__main__':
    # answer = 6
    # input = 3 \n 7
    N = int(input())
    K = int(input())

    print(findK(N, K))
