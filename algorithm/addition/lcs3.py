# LCS, LCS3
# 첫 줄에는 첫 번째 문자열이, 둘째 줄에는 두 번째 문자열이, 셋째 줄에는 세 번째 문자열이 주어진다.
# 첫 번째 문자열과 두 번째 문자열과 세 번째 문자열의 LCS의 길이를 출력하라

import sys
input = sys.stdin.readline

seq_1 = input().rstrip()
seq_2 = input().rstrip()
seq_3 = input().rstrip()

x = len(seq_1)
y = len(seq_2)
z = len(seq_3)

arr = [[[0] * (z+1) for _ in range(y+1)] for _ in range(x+1)]

for i in range(1, x+1):
    for j in range(1, y+1):
        for k in range(1, z+1):
            if seq_1[i-1] == seq_2[j-1] and seq_2[j-1] == seq_3[k-1]:
                arr[i][j][k] = arr[i-1][j-1][k-1] + 1
            
            else:
                arr[i][j][k] = max(arr[i][j][k-1], arr[i][j-1][k], arr[i-1][j][k])

ans = -1

for i in range(x+1):
    for j in range(y+1):
        ans = max(max(arr[i][j]), ans)

print(ans)