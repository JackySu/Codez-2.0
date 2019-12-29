def reject(s):
    return s.replace(" ", "")


s = input()
s_nospace = reject(s)

li = []
nu = 1
for n in s_nospace:
    if n == "0":
        li.append(nu)
    nu += 1

print(len(li), li)
