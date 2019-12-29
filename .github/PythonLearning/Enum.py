from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print(name, '->', member, ',', member.value)
# 上面这种写法更加适用于有重复值的遍历

for date in Month:
    print(date.name, '->', date.value)
