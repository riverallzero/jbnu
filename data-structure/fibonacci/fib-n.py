def fib(n: int, cache: dict = {1: 1, 2: 1}) -> int:
    if n in cache:
        return cache[n]

    cache[n] = fib(n - 1, cache) + fib(n - 2, cache)

    return cache[n]


if __name__ == '__main__':
    print(fib(1)) # 1
    print(fib(3)) # 2
    print(fib(5)) # 5
    print(fib(10)) # 55
    print(fib(1000)) # 434665...