def make_table(pattern):
    pattern_size = len(pattern)
    table = [0] * pattern_size
    
    # 첫 글자는 0으로 시작
    matched_length = 0
    
    # 두 번째 글자부터 체크
    for current_pos in range(1, pattern_size):
        # 이전에 일치했던 문자들을 확인
        while matched_length > 0 and pattern[current_pos] != pattern[matched_length]:
            matched_length = table[matched_length - 1]
            
        # 현재 위치의 문자가 일치하면
        if pattern[current_pos] == pattern[matched_length]:
            matched_length += 1
            table[current_pos] = matched_length
            
    return table

if __name__ == '__main__':
    L = int(input().strip())
    pattern = input().strip()
    
    table = make_table(pattern)
    print(L-table[-1])
    