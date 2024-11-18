import sys

def ctrMin(K, datas):    
    datas.sort(reverse=True)
    ctr = 0

    for data in datas:
        ctr += K // data
        K %= data

    return ctr

if __name__ == '__main__':
    # answer = 6
    # inputs = [
    #     '10 4200\n',
    #     '1\n',
    #     '5\n',
    #     '10\n',
    #     '50\n',
    #     '100\n',
    #     '500\n',
    #     '1000\n',
    #     '5000\n',
    #     '10000\n',
    #     '50000'
    # ]

    inputs = sys.stdin.readlines()

    N, K = map(int, inputs[0].split())
    datas = list(map(int, inputs[1:]))

    print(ctrMin(K, datas))
