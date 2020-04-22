def bracket(s):
    BracketDict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    if s == '':
        return True
    else:
        length = len(s)
        for i in range(length):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                flag = False
                revList = list(range(i + 1, length))
                revList.reverse()
                for j in revList:
                    if s[j] == BracketDict[s[i]]:
                        if bracket(s[i + 1: j]):
                            flag = True
                            break
                if not flag:
                    return False
        return True


s = input()
print(bracket(s))
