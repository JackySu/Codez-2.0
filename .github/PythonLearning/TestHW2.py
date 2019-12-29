'''
Str = input()
List = list(map(int, Str.strip().split()))
print(List)
'''
exDict = {1: 1, 2: 1, 3: 3, 4: 2, 5: 7, 6: 18, 7: 7, 8: 14, 9: 20, 10: 14}
OcrDict = {}

for key in exDict.values():
    n = OcrDict.get(key, -1)
    if n != -1:
        OcrDict[key] += 1
    else:
        OcrDict[key] = 1

for key in OcrDict.keys():
    if OcrDict[key] == 1:
        print(key)

