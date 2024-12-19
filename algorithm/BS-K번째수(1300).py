# Binary Search, K번째수
# 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다.
# 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구하라

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
