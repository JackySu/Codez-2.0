def plus(res, num):
    return res + num


def minus(res, num):
    return res - num


def by(res, num):
    return res * num


def div(res, num):
    return res / num


if __name__ == "__main__":
    switch = {
        "+": plus,
        "-": minus,
        "*": by,
        "/": div
    }

    operations = list(input().strip().split())
    res = int(operations[0])

    for i in [x for x in range(len(operations)) if x % 2 == 1]:
        try:
            res = switch[operations[i]](res, int(operations[i + 1]))
        except KeyError as e:
            print(e)

    print(res)
