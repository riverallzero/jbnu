# BFS & DFS, N-Queen 2
# 퀸 N개를 서로 공격할 수 없게 퀸을 놓는 방법 한 가지를 출력하라
# = N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 한가지 경우를 출력하라

n = int(input())
t = n//2
ans = []
if n%6 == 2:
    for i in range(1, t+1):
        print(i*2)
    print(3)
    print(1)
    for i in range(3, t):
        print(i*2 + 1)
    print(5)
elif n%6 == 3:
    for i in range(2, t+1):
        print(i*2)
    print(2)
    for i in range(2, t+1):
        print(i*2 + 1)
    print(1)
    print(3)
else:
    for i in range(1,t+1):
        print(i+t)
        print(i)
    if n&1:
        print(n)
        