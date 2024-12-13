import sys

def maxCtr(ranks):
    ranks.sort()

    counts = 1
    max_rank = 1000

    for n in range(N):
        if n == 0:
            max_rank = ranks[n][1]
            continue
        else:
            if ranks[n][1] < max_rank:
                max_rank = ranks[n][1]
                counts += 1

    return counts

if __name__ == '__main__':
    T = int(input()) 

    for _ in range(T):
        N = int(input()) 
        ranks = []

        for _ in range(N):
            ranks.append(list(map(int, sys.stdin.readline().split())))

        print(maxCtr(ranks))
