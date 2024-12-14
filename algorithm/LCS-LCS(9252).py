import sys

def find(A, B):
    if A == B:
        return A
    
    arr = [['' for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i-1] == B[j-1]:
                # 대각선 값에 현재 값 더하기
                arr[i][j] = arr[i-1][j-1] + A[i-1]
            else:
                # 왼쪽, 위쪽 중 더 큰 값 고르기
                if len(arr[i-1][j]) >= len(arr[i][j-1]):
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = arr[i][j-1]

    return arr[-1][-1]


if __name__ == '__main__':
    # answer = 4 \n ACAK
    # inputs = [
    #     'ACAYKP\n',
    #     'CAPCAK'
    # ]

    inputs = sys.stdin.readlines()

    A, B = inputs[0].strip(), inputs[1]

    sequence = find(A, B)

    print(len(sequence))
    if sequence:
        print(sequence)
        