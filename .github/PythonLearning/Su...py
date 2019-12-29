def _odd_iterator():
    n = 1
    while 1:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iterator()
    while 1:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


m = int(input())
if m == 2:
    print('2')
else:
    for n in primes():
        if n <= m:
            print(n)
        else:
            break
