letterComb = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

digits = input()
ans = ['']
for num in digits:
    ans = [pre+suf for pre in ans for suf in letterComb[num]]

print(ans)
