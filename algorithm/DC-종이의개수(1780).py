import sys

def findCtr(N, arr):
    val_ctr = {'-1': 0, '0': 0, '1': 0}

    def splitFind(a, b, c, d):
        init_val = arr[a][c]
        is_same = True

        for i in range(a, b):
            for j in range(c, d):
                if arr[i][j] != init_val:
                    is_same = False
                    break
            if not is_same:
                break

        if is_same:
            val_ctr[str(init_val)] += 1
        else:
            n = (b - a) // 3  
            for i in range(3): 
                for j in range(3):
                    splitFind(a + i * n, a + (i + 1) * n, c + j * n, c + (j + 1) * n)

    splitFind(0, N, 0, N)

    return val_ctr

if __name__ == '__main__':
    # answer
    #     10
    #     12
    #     11 
    # inputs = [
    #     '9\n',
    #     '0 0 0 1 1 1 -1 -1 -1\n',
    #     '0 0 0 1 1 1 -1 -1 -1\n',
    #     '0 0 0 1 1 1 -1 -1 -1\n',
    #     '1 1 1 0 0 0 0 0 0\n',
    #     '1 1 1 0 0 0 0 0 0\n',
    #     '1 1 1 0 0 0 0 0 0\n',
    #     '0 1 -1 0 1 -1 0 1 -1\n',
    #     '0 -1 1 0 1 -1 0 1 -1\n',
    #     '0 1 -1 1 0 -1 0 1 -1',
    # ]

    inputs = sys.stdin.readlines()

    N = int(inputs[0])
    arr = [val.split() for val in inputs[1:]]

    results = findCtr(N, arr)
    for result in results.values():
        print(result)