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


def operate(operations, operate_lvl_li, begin, end):
    for lvl in operate_lvl_li:
        i = begin
        while i < end - 1 and len(operations) != 1:
            try:
                if operations[i] == '(':
                    find_bracket = list(range(i + 1, len(operations)))
                    find_bracket.reverse()
                    for j in find_bracket:
                        if operations[j] == ')' and j - i > 2:
                            operate(operations, operate_lvl_li, i + 1, j - 1)
                        elif j - i == 2:
                            operations.pop(i)
                            operations.pop(j - 1)
                            end -= 2
                else:
                    try:
                        operations[i] = switches[lvl][operations[i + 1]](int(operations[i]), int(operations[i + 2]))
                        pop_item(operations, i + 1, 2)
                        end -= 2
                    except ValueError:
                        i += 2
            except KeyError or IndexError:
                i += 2


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

    operate(operations, operate_lvl_li, 0, len(operations))

    print(operations[0])
