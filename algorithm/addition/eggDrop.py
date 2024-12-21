# 계란 2개와 빌딩의 높이(n) 주어질 때, 계란이 깨지는 층이 몇 층인지 알기 위해서는 총 몇 번 던져봐야하는지 구하라.

def twoeggDrop(n):
    dp = [[i for i in range(n+1)],[0 for _ in range(n+1)]] # [[계란이 1개인 경우], [계란이 2개인 경우]]
    jump = 1 # 값을 일정하게 증가시키기 위함
    for start in range(1, n+1):
        while (jump < start) and (max(dp[0][jump-1],dp[1][start-jump])) > max(dp[0][jump], dp[1][start-jump-1]):
            jump += 1
        dp[1][start] = 1 + max(dp[0][jump-1], dp[1][start-jump])
    return dp[1][n]

print(twoeggDrop(100))  # 14
