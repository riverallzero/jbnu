def nQueen(n):
    counts = 0
    def backTracking(row):
        nonlocal counts
        if row == n:
            counts += 1
            return counts

        for j in range(n if row else n//2):
            if not col[j] and not d1[row-j] and not d2[row+j]:
                col[j] = True
                d1[row-j] = True # ↘ 
                d2[row+j] = True # ↙

                backTracking(row+1)

                col[j] = False
                d1[row-j] = False
                d2[row+j] = False

    col = [False for _ in range(n)]
    d1 = [False for _ in range(n*2)]
    d2 = [False for _ in range(n*2)]

    if n % 2: # 홀수: 절반 계산 후 중앙 열의 경우를 추가적으로 계산
        backTracking(0)
        counts *= 2
        j = n//2
        col[j] = d1[-j] = d2[j] = True
        backTracking(1)
    else: # 짝수: 절반만 계산한 뒤 결과를 2배로 곱합
        backTracking(0)
        counts *= 2

    return counts

if __name__ == '__main__':  
    N = int(input())
    print(nQueen(N))
