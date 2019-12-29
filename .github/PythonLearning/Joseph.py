def Joseph(n, m):
    if n <= 1:
        return n - 1
    return (Joseph(n - 1, m) + m) % n


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    print(Joseph(n, m))
