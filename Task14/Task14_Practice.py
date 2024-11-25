#7761
x = 4**2020 + 2**2017 - 15
s = []
while x != 0:
    s.append(x % 2)
    x = x // 2

print(s.count(1))

