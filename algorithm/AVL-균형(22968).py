import sys

if __name__ == '__main__':
    inputs = sys.stdin.readlines()

    for line in inputs[1:]:
        v = int(line.strip())
        a = 1
        b = 2
        max_height = 0
        
        while a <= v:
            a, b = b, a + b + 1 # 피보나치 수열로 계산(수정) b = a + b -> b = a + b + 1
            max_height += 1
        print(max_height)
