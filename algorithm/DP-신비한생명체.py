# DP, 신비한 생명체
def totalAdult(N, M):
    MOD = 1000000007
    
    # 0: 분열법 어른, 1: 알 어른
    dp = [[0] * 2 for _ in range(M + 1)]
    
    maturing_from_egg = [0] * (M + 1)      # 알에서 태어남
    maturing_from_fission = [0] * (M + 1) # 분열법으로 태어남
    hatching_eggs = [0] * (M + 1)         # 알에서 부화함
    
    # 초기 조건 설정
    if M >= 4:
        maturing_from_egg[4] = N
        dp[4][0] = N  # 초기 성체 개체 수도 설정
    
    for day in range(M + 1):
        # 이전 날의 성인 수를 유지
        if day > 0:
            dp[day][0] = dp[day-1][0]
            dp[day][1] = dp[day-1][1]
        
        # 성인이 되는 개체 추가
        if day >= 4:
            dp[day][0] = (dp[day][0] + maturing_from_egg[day]) % MOD
        if day >= 2:
            dp[day][1] = (dp[day][1] + maturing_from_fission[day]) % MOD
            
        # 분열 생식 (3일마다)
        if day >= 3 and day % 3 == 0:
            if day + 2 <= M:
                maturing_from_fission[day + 2] = (maturing_from_fission[day + 2] + dp[day][0]) % MOD
        
        # 알 낳기 (5일마다)
        if day >= 5 and day % 5 == 0:
            if day + 3 <= M:
                hatching_eggs[day + 3] = (hatching_eggs[day + 3] + dp[day][1]) % MOD
        
        # 알이 부화하고 성장
        if day >= 3 and day + 4 <= M:
            maturing_from_egg[day + 4] = (maturing_from_egg[day + 4] + hatching_eggs[day]) % MOD
    
    return (dp[M][0] + dp[M][1]) % MOD

if __name__ == '__main__':
    N, M = map(int, input().split()) #  N=4, M=100
    print(totalAdult(N, M)) # 37944368
