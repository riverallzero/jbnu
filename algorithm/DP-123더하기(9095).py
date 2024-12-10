import sys

def findCtr():
    ctr_arr = [0] * 11

    ctr_arr[0] = 1 # 1
    ctr_arr[1] = 2 # 1+1, 2
    ctr_arr[2] = 4 # 1+1+1, 2+1, 1+2, 3

    for i in range(3, 11):
        ctr_arr[i] = ctr_arr[i-1] + ctr_arr[i-2] + ctr_arr[i-3]

    return ctr_arr

if __name__ == '__main__':
    # answer = 
    #     7
    #     44
    #     274
    # inputs = [
    #     '3\n',
    #     '4\n',
    #     '7\n',
    #     '10\n'
    # ]
    
    inputs = sys.stdin.readlines()

    N = int(inputs[0])
    cases = list(map(int, inputs[1:]))

    ctr_arr = findCtr()

    for case in cases:
        print(ctr_arr[case-1])
