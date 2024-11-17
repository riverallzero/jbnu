import sys

def mulMat(M1, M2):
    global N

    M = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                M[i][j] += M1[i][k] * M2[k][j] 
                M[i][j] %= 1000
    
    return M

def sqrS(B, M):
    if B == 1:
        return [[val%1000 for val in row] for row in M]
    
    tmp_M = sqrS(B//2, M)
    
    if B % 2 == 0:
        return mulMat(tmp_M, tmp_M)
    else:
        return mulMat(mulMat(tmp_M, tmp_M), M)

if __name__ == '__main__':
    # answer
    #     69 558
    #     337 406
    # inputs = [
    #     '2 5\n',
    #     '1 2\n',
    #     '3 4\n'
    # ]

    inputs = sys.stdin.readlines()

    N, B = map(int, inputs[0].split())
    matrix = [list(map(int, input.split())) for input in inputs[1:]]
    result_matrix = sqrS(B, matrix)
    
    for row in result_matrix:
        print(*row)
