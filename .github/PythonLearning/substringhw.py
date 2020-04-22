def hw(ch):
    if ch == ch[::-1]:
        return True
    else:
        return False


s = input()

n = len(s)
if n == 1:
    print(s)
else:
    i, j, StartIndex, EndIndex, maxl = 1, 1, 0, 0, 1
    # j for left index, i for right
    while i < n:
        if s[j - 1] == s[i + 1]:
            j -= 1
            i += 1
            if i - j + 1 > maxl:
                StartIndex = j
                EndIndex = i
                maxl = i - j + 1
        else:
            for k in range(j, i + 1):
                if hw(s[k: i + 1]):
                    j = k
                    if i - j + 1 > maxl:
                        StartIndex = j
                        EndIndex = i
                        maxl = i - j + 1
                    break
            i += 1
            j -= 1

    print(s[StartIndex: EndIndex + 1])
