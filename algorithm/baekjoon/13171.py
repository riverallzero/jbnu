import sys

def makeList(A, X):
    val_dict = {}

    init_val = A
    init_power = 1

    val_dict[1] = A
    while init_power < X:
        init_val = init_val * init_val

        if init_val >= 1000000007:
            init_val %= 1000000007

        if init_power * 2 <= X:
            val_dict[init_power * 2] = init_val

        init_power *= 2

    return val_dict

def makeBin(X):
    bit_arr = []

    while X > 0:
        remain = X % 2
        bit_arr.append(remain)
        X //= 2

    key_arr = []
    for v, val in enumerate(bit_arr):
        if val == 1:
            key_arr.append(2**v)

    return key_arr

def calPower(A, X):
    val_dict = makeList(A, X)
    key_arr = makeBin(X)

    result = 1
    for idx in key_arr:
        result *= val_dict[idx]

        if result >= 1000000007:
            result %= 1000000007

    return result

if __name__ == '__main__':
    # answer = 27
    # inputs = [
    #     '100\n',
    #     '100'
    # ]

    inputs = sys.stdin.readlines()

    A, X = map(int, inputs)
    
    print(calPower(A, X))
