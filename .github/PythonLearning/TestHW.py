'''
Gtuple = ('apple', 'grape', 'orange', 'pineapple', 'peach')
GList = list(Gtuple)
i = 0
for j in GList:
    if j == 'pineapple':
        GList.pop(i)
    i += 1
print(tuple(GList))

gList = [24, 55, 16, 44, 23, 24]
for i in gList:
    print(f'({gList.index(i):02d}, {i:02d})')
'''
from bs4 import BeautifulSoup

# the usage of index() may cause error
# due to index() introduces the first index that matches the item of list
html_doc = """

<html><head><title>学习python的正确姿势</title></head>
<body>
<p class="title"><b>小帅b的故事</b></p>

<p class="story">有一天，小帅b想给大家讲两个笑话
<a href="http://example.com/1" class="sister" id="link1">一个笑话长</a>,
<a href="http://example.com/2" class="sister" id="link2">一个笑话短</a> ,
他问大家，想听长的还是短的？</p>

<p class="story">...</p>

"""

# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.find_all('a'))
# print(soup.a)
# print(soup.find(id='link2'))
# print(soup.get_text())
# print(soup.select("p > #link1"))  # output be in list form
# print(len('wojCgnbCjWFYc8KLwoFwwoLChlxwbHnCjWl9wpdlWHN-woFwwobChlxkbHnCl8KCfQ=='))

# raw = input()
# for char in raw:
#     if char not in [0-9]:
#         print('Not Number')
#         break

list1 = [1, 2, 5, 9]
list2 = [3, 8, 4, 2]
list1.extend(list2)
print(list1)


def m(x, y):
    x = 3
    y[0] = 3


a = 0
b = [None]
m(a, b)
print(a, b)


list1 = [1, 3, 5, 42, 6, 723, 36, 54, 5]
print(max(list1))
