def canPut(c, r):
    for c_col in range(c):
        q_row = queen_col_locs[c_col]

        if q_row == r: # 같은 행에 위치한 경우
            return False
        elif abs(q_row-r) == abs(c-c_col): # 대각선에 위치한 경우
            return False
        
    return True

def dfs(c):
    case_ctr = 0

    if c == N:
        return 1

    for n in range(N):
        if canPut(c, n):
            queen_col_locs[c] = n 
            case_ctr += dfs(c+1) # 열 +1씩 증가시키며 탐색 후 경우의 수 세기
            queen_col_locs[c] = None # 다시 탐색하도록 초기화

    return case_ctr

if __name__ == '__main__':  
    N = int(input())
    queen_col_locs = [None for _ in range(N)] # 퀸은 무조건 열에 1개 이하 존재, 열별로 어떤 행에 퀸이 놓여있는지 나타냄
    
    result = dfs(0)
    print(result)
