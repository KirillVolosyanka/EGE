# Number 1

'''for a in range(0, 1000):
     Ok = True
     for x in range(0, 1000):
         for y in range(0, 1000):
             if (2*x + 3*y >= 40) or ((x < a) and (y <= a)) == True:
                 Ok = False
                 break
     if Ok:
        print(a)
'''
# Answer: done

# Number 2

'''for a in range(0, 1000):
     Ok = True
     for x in range(0, 1000):
         for y in range(0, 1000):
             if (2*x + 3*y >= 40) or ((x < a) and (y <= a)) == True:
                 Ok = False
                 break
     if Ok:
        print(a)
'''
# Answer: done

'''_________________________________________________________________________'''

# Number 3
#we tried to do it together, but this shit didn't work, nothing've changed
def func(x, up,down):
    return ((not(down <= x and x <= up) or (x**2 <= 100)) and (not(x**2 <= 64) or (down <= x and x <= up)))

for down in range(-100, 100):
    for up in range (down +1, 500 +1):
        ok = True
        for x in range (-1000, 1000):
             f = func(x,up, down)
             if f == False:
                ok = False
                break
        if ok:
                print(up - down)
# Answer: _ _ _ _

'''_________________________________________________________________________'''

# Number 4

'''for a in range(0,100):
    ok = True
    for x in range(0,100):
        for y in range(0,100):
            if ((x < a) or (y < a) or (x + 2*y > 50)) == False:
                ok = False
                break
    if ok:
        print(a)
        break'''
# Answer: 17 Right

'''_________________________________________________________________________'''

# Number 5
'''for a in range(0, 300):
    ok = True
    for x in range(0, 300):
        for y in range(0, 300):
            if ((x * y < 120) or (y > a) or (x > a)) == False:
                ok = False
                break

    if ok:
        print(a)'''
# Answer: 10 Right

'''_________________________________________________________________________'''

# Number 6
'''for a in range(0,1000):
    ok = True
    for x in range(0,1000):
        for y in range(0, 1000):
            if ((x + 2*y > 48) or (y>x) or (x + 3* y<a)) == False:
                ok = False
                break
    if not(ok):
        print(a)'''
# Answer: 64 Right

'''_________________________________________________________________________'''

# Number 7
'''for a in range(0,500):
    ok = True
    for x in range(0,500):
        for y in range(0,500):
            if ((x + 3 * y > a) or (x <30) or (y < 30)) == False:
                ok = False
                break
    if ok:
        print(a)'''

# Answer: 119 Right

'''_________________________________________________________________________'''

# Number 8
'''for a in range(0,500):
    ok = True
    for x in range(0,500):
        for y in range(0,500):
            if ((4*x + 3 *y <a) or (x>y) or (y>13)) == False:
                ok = False
                break
    if ok:
        print(a)
        break'''
# Answer: 92 Right

'''_________________________________________________________________________'''

# Number 9
'''for a in range(0,500):
    ok = True
    for x in range(0,500):
        for y in range(0, 500):
            if ((x * y <121) or (y > a) or (x >= a)) == False:
                ok = False

    if ok:
        print(a)'''
# Answer: 11 Right

'''_________________________________________________________________________'''

# Number 10
'''for a in range(0,500):
    ok = True
    for x in range(0,500):
        for y in range(0,500):
            if ((2*x +3*y != 60) or (a>= x) or (a >= y)) == False:
                ok = False
                break
    if ok:
        print(a)
        break'''
# Answer: 12 Right

'''_________________________________________________________________________'''

# Number 11
#For who's sake I've got 5 more tasks, we have only 10 in HW)

# I just forgot correct this file)))