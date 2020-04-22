s = input().strip(' ')

res = [-1, len(s)]
for i in range(len(s)):
    if (s[i] == '-' or s[i] == '+') and len(s) != 1:
        res[0] = i
        break
    else:
        try:
            ch = int(s[i])
        except ValueError:
            break
        if isinstance(ch, int):
            res[0] = i
            break

if res[0] == -1:
    print(0)
else:
    j = 0
    for j in range(res[0] + 1, len(s)):
        try:
            ch = int(s[j])
        except ValueError:
            j -= 1
            break
    try:
        num = int(s[res[0]: j + 1].strip('.'))
    except ValueError:
        num = 0
    if num < -2147483648:
        print(-2147483648)
    elif num > 2147483647:
        print(2147483647)
    else:
        print(num)
