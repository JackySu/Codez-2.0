def pop_item(li, i1, times):
    for i in range(times):
        try:
            li.pop(i1)
        except IndexError:
            pass


def plus(res, num):
    return res + num


def minus(res, num):
    return res - num


def by(res, num):
    return res * num


def div(res, num):
    return res / num


if __name__ == "__main__":

    # - 计算优先级数 - #
    operate_level = 2
    ###################

    operate_lvl_li = list(range(1, operate_level + 1))
    operate_lvl_li.reverse()

    switch_lvl1 = {
        "+": plus,
        "-": minus
    }

    switch_lvl2 = {
        "*": by,
        "/": div
    }

    switches = {
        1: switch_lvl1,
        2: switch_lvl2
    }

    operations = list(input().strip().split())

    for lvl in operate_lvl_li:
        i = 0
        while i < len(operations) - 2:
            try:
                operations[i] = switches[lvl][operations[i + 1]](int(operations[i]), int(operations[i + 2]))
                pop_item(operations, i + 1, 2)
            except KeyError or IndexError:
                i += 2

    print(operations[0])
