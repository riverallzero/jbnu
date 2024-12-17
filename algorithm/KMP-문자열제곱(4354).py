def result(text):
    if not text: 
        return 0
        
    length = len(text)
    pattern_table = make_table(text)
    
    # 반복되는 패턴 길이
    pattern_length = length - pattern_table[-1]
    
    # 입력 문자열 길이가 패턴 길이로 나눠지지 않으면 안됨
    if length % pattern_length != 0:
        return 1
        
    # 반복되느느 패턴인지 확인
    base_string = text[:pattern_length]
    if base_string * (length // pattern_length) == text:
        return length // pattern_length
    
    return 1

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
    while True:
        text = input().strip()

        if text == '.':
            break
        else:
            print(result(text))
