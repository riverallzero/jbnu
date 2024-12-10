def nQueen(c, cols, left_2_right, right_2_left):
    global N
    
    if c == N:
        return 1  # 모든 열에 퀸을 배치한 경우
    
    case_ctr = 0
    for r in range(N):
        if not cols[r] and not left_2_right[c + r] and not right_2_left[c - r + N - 1]:
            # 상태 업데이트
            cols[r] = left_2_right[c + r] = right_2_left[c - r + N - 1] = True
            case_ctr += nQueen(c + 1, cols, left_2_right, right_2_left)
            
            # 상태 복구
            cols[r] = left_2_right[c + r] = right_2_left[c - r + N - 1] = False

    return case_ctr

if __name__ == '__main__':  
    # N=8, answer=92
    N = int(input())

    cols = [False] * N # 각 열에 퀸이 있는지 여부
    left_2_right = [False] * (2 * N) # \ 대각선 사용 여부 (r+c)
    right_2_left = [False] * (2 * N) # / 대각선 사용 여부 (r-c+N-1)
    
    print(nQueen(0, cols, left_2_right, right_2_left))
