# Greedy, 신입사원
# 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다
# 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.
# 이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하라

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
