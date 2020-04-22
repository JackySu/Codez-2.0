'''nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
k = 2
'''

'''nums = [1,1,2,1,1]
k = 3
'''
'''
nums = [2,4,6]
k = 1
'''

l = len(nums)

oddCounter = 0

oddIndex = [-1]

for i in range(l):
    if nums[i] % 2 == 1:
        oddCounter += 1
        oddIndex.append(i)

oddIndex.append(l)

if oddCounter < k:
    print(0)
else:
    res = 0
    for i in range(1, oddCounter - k + 2):
        res += (oddIndex[i] - oddIndex[i - 1]) * (oddIndex[i + k] - oddIndex[i + k - 1])
    
    print(res)
