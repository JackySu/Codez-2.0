def _is_hw(n):
    l = len(n)
    if l % 2 == 0:
        if n[:l // 2: 1] == n[:l // 2 - 1: -1]:
            return True
        else:
            return False
    else:
        if n[:l // 2: 1] == n[:l // 2: -1]:
            return True
        else:
            return False


x = input()
print(_is_hw(x))
