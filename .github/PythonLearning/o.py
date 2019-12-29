def fib(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a + b
        n -= 1


n = int(input())
g = fib(n)
while 1:
    try:
        x = next(g)
        print(x)
    except StopIteration:
        break


def a():
    pass


def b():
    pass
