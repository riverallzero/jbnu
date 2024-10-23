def fib(n: int) -> int:

    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(1)) # 1
    print(fib(3)) # 2
    print(fib(5)) # 5
    print(fib(10)) # 55
    print(fib(1000)) # Recursion Error: maximum recursion depth exceeded in comparison