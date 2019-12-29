x = int(input())
y = int(input())
x, y = max(x, y), min(x, y)
z = -1

while z != 0:
    z = x % y
    x, y = y, z

print(x)
