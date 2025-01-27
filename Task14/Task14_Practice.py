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

'''x = 9**8 + 3**5 - 9
s = []
while x != 0:
    s.append(x%3)
    x = x//3

print(s.count(2))'''

#alt
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

#48377

'''for x in "0123456789ABC":
    x1 = '26' + str(x) + "98"
    x2 = "4" + str(x) + "296"
    res = int(x1, 13) + int(x2,13)
    if res % 34 == 0:
        res //= 34
        print(res)'''

#48394

'''for x in "0123456789ABC":
    x1 = "4C" +str(x) +'4'
    x2 = str(x) +'62A'
    res = int(x1,15) + int(x2,13)
    if res % 121 == 0:
        res //= 121
        print(res)'''

#48402

'''for x in '0123456789AB':
    x1 = "3" + x + "DA"
    x2 = "5" + x + "A6"
    res = int(x1,14) + int(x2,12)
    if res % 81 == 0:
        res //= 81
        print(res)'''

#48384

'''for x in "012345678":
    for y in "012345678":
        x1= "88" + x+'4' + y
        x2= '7' + x+ "44" + y
        res = int(x1,9) + int(x2,11)
        if res % 61 == 0:
            res//=61
            print(res)'''

#48389

'''for x in '0123456':
    for y in '0123456':
        x1 = y + x + "320"
        x2 = '1' + x + '3' + y +'3'
        res = int(x1, 7) + int(x2,9)

        if res % 181 == 0:
            res//=181
            print(res)'''

#48386
'''for x in '0123456789ABCDE':
    for y in '0123456789ABCDE':
        x1 = "90" + x + "4" + y
        x2 = '91' + x + y + "2"
        res = int(x1, 15) + int(x2,16)
        if res % 56 == 0:
            res //= 56
            print(res)'''

#63063
'''def f(n):
    n = str(n)
    res = 0
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
        res += s[i] * 39 ** i
    return res

for x in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#":
    for y in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#":
        x1 = "58" + x + "723" + y + '49'
        res = f(x1)
        if res % 38 == 0:
            if f(y + x) **0.5 % 1 == 0:
                print(f(y + x))'''
'''
d1 = 5*39**8 + 8*39**7 + 7*39**5 + 2*39**4 + 3*39**3 + 4*39**1 + 9  # постоянная часть числа не меняющаяся в цикле
for x in range(1,39):
    for y in range(1,39):
        d = d1 + x*39**6 + y*39**2  # переменная часть числа
        if d % 38 == 0 and ((y*39**1 + x)**0.5 - int((y*39**1 + x)**0.5)) == 0: # условие поставленное в задаче
#           print(d)
#           m = 38
            print("    x,y =", x, y)
            otvet = (y*39**1 + x)
            print(otvet)
'''
'''
from datetime import datetime
t = datetime.now()
dx=39**4
x = 0
y = 38
while not((x*dx + y) % 38 == 0 and ((y*39 + x)**0.5).is_integer()):
    x += 1
    y -= x
t1 = datetime.now()
print(x*dx + y)
print(x, y)
print('RESULT -', (y*39 + x))
print(t1-t)'''

def conv(n, sys):
    res = ''
    while n:
        res = str(n % sys) + res
        n //= sys
    return res