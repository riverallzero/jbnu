# KMP, 찾기
# 두 개의 문자열 P와 T에 대해, 문자열 P가 문자열 T 중간에 몇 번, 어느 위치에서 나타나는지 알아내는 문제=문자열 매칭 
# T와 P가 주어졌을 때, 문자열 매칭 문제를 해결하는 프로그램

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

def find_pattern(text, pattern):
    # 패턴 위치 저장
    positions = []
    pattern_table = make_table(pattern)
    
    text_size = len(text)
    pattern_size = len(pattern)
    matched_length = 0
    
    for text_pos in range(text_size):
        # 불일치가 발생할 경우, 테이블을 참조하여 다음 비교 위치로 이동
        while matched_length > 0 and text[text_pos] != pattern[matched_length]:
            matched_length = pattern_table[matched_length - 1]
            
        # 현재 위치의 문자가 일치하면
        if text[text_pos] == pattern[matched_length]:
            matched_length += 1
            # 패턴을 모두 찾았으면
            if matched_length == pattern_size:
                # 시작 위치를 저장 (1부터 시작하는 인덱스 사용)
                positions.append(text_pos - pattern_size + 2)
                # 다음 탐색을 위해 테이블 참조
                matched_length = pattern_table[matched_length - 1]
    
    return len(positions), positions

if __name__ == '__main__':
    text = input().strip() # ABC ABCDAB ABCDABCDABDE
    pattern = input().strip() # ABCDABD
    
    count, positions = find_pattern(text, pattern)
    
    print(count) # 1
    if positions:
        print(*positions) # 16
