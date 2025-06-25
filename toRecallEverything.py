'''from turtle import *

screensize(2000,200)
k = 30
lt(90)
down()
tracer(90)

for i in range(7):
    rt(45)
    fd(k*11)
    rt(45)

up()

for x in range(-30,30):
    for y in range(-30,30):
        goto(x*k,y*k)
        dot(3,"green")
done()'''

'''a = open("n9recall")
c = 0

for line in a:
    line = [int(i) for i in line.split()]
    res = [line.count(j) for j in line]

    if res.count(2) == 2 and res.count(1) == 4:
        repSum = 0
        nonRepSum = 0
        for i in range(len(line)):
            if res[i] == 2:
                repSum += line[i]
            else:
                nonRepSum += line[i]

        nonRepAv = nonRepSum // 4

        if nonRepAv <= repSum:
            c+=1
print(c)'''

'''a = open("n9recall")
c = 0

for line in a:
    line = [int(i) for i in line.split()]
    res = [line.count(j) for j in line]

    lineSum = sum(line)
    maxMin = max(line) + min(line)

    remSum2 = (lineSum - maxMin)*2
    maxMin3 = maxMin*3

    if res.count(1) == 5 and maxMin3 <= remSum2:
        c+=1
print(c)'''

from ipaddress import *

'''for x in range(0,15):
    for y in range(0,15):
        d1 = 9*15**4 + 0*15**3 + x*15**2 + 4*15**1 + y*15**0
        d2 = 9*16**4 + 1*16**3 + x*16**2 + y*16**1 + 2*16**0
        res = d1 + d2

        if res % 56 == 0:
            print(res//56)'''

'''P = [i for i in range(130,172)]
Q = [i for i in range(150,186)]

for a_down in range(130,186):
    for a_up in range(a_down+1,186):
        ok = True
        A = [i for i in range(a_down,a_up+1)]
        for x in range(-3000,3000):
            f = not(x in P) or (not((x in Q) and not(x in A)) or not(x in P))
            if f == False:
                ok = False

        if ok:
            print(a_up - a_down)'''

#Петя не может выиграть за один ход,
# при любом ходе Пети
# Ваня может выиграть своим первым ходом
'''def f(x,h):
    if h == 3 and x >=38:
        return 1
    if h == 3 and x <38:
        return 0
    if h < 3 and x >=38:
        return 0
    else:
        if h % 2 == 0:
            return f(x+1,h+1) or f(x*3,h+1)
        else:
            return f(x+1,h+1) and f(x*3,h+1)


def f5(x,h):
    if (h == 3 or h == 5) and x >= 38:
        return 1
    if h == 5 and x < 38:
        return 0
    if h < 5 and x >= 38:
        return 0
    else:
        if h % 2 == 0:
            return f5(x + 1, h + 1) or f5(x * 3, h + 1)
        else:
            return f5(x + 1, h + 1) and f5(x * 3, h + 1)

for s in range(1,38):
    if (f5(s,1) == True) and (f(s,1) == False):
        print(s)'''

'''from fnmatch import *
for i in range(0,10**8,317):
    if fnmatch(str(i), "12??1*56"):
        print(i,i//317)'''

a = open("24 (5).txt").readline()

a = (a.replace("A","G").replace("O","G")
     .replace("C","S").replace("D"))