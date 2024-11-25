#7761
'''
x = 4**2020 + 2**2017 - 15
s = []
while x != 0:
    s.append(x % 2)
    x = x // 2

print(s.count(1))'''

#9367
'''x = 9**8 + 3**5 - 9
s = []
while x != 0:
    s.append(x%3)
    x = x//3

print(s.count(2))'''

#13743
'''
x = 7**20 + 7**30 - 7**2
s = []
words = "ABCDE"
while x != 0:
    if (x % 15 > 9):
        s.append(words[x%15 // 10])
    else:
        s.append(x%15)
    x = x // 15
s = s.reverse()
print(s)'''

#47218
'''
for x in '0123456789ABCDE':
    x1 = '123' + str(x) + '5'
    x2 = '1' + str(x) + '233'
    res = int(x1, 15) + int(x2, 15)
    if res % 14 == 0:
        res = res // 14
        print(res)'''

def hui(n):
    n = str(n)
    cunt = 0
    s = []
    for i in range(len(n) - 1, -1, -1):
        if n[i] =="!" or n[i] =="@" or n[i] =="#":
            if n[i] == "!":
                s.append(36)
            if n[i] == "@":
                s.append(37)
            if n[i] == "#":
                s.append(38)
        else:
            s.append(int(n[i], 36))

    for i in range(0,len(s)):
        cunt += s[i] * 39**i
    return cunt

for x in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#":
    for y in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#":
        x1 = "58" + x + "723" + y + '49'
        res = hui(x1)
        if res % 38 == 0:
            if hui(y + x)**0.5 % 1 == 0:
                print(hui(y + x))