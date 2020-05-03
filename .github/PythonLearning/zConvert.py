s = "ABCDE"
numRows = 4

'''
"PAYPALISHIRING"
3
'''

if s == '':
    print(s)
if numRows == 1:
    print(s)


res = ''
for i in range(numRows):
    if i == 0 or i == numRows - 1:
        res = res + s[i::2 * numRows - 2]
    else:
        j = 0
        while j <= len(s) + 2 * numRows - 1:
            try:
                if j - i >= 0:
                    if j + i < len(s):
                        res = res + s[j - i] + s[j + i]
                    else:
                        res = res + s[j - i]
                else:
                    res = res + s[j + i]
            except IndexError:
                pass
            j += 2 * numRows - 2

print(res)
