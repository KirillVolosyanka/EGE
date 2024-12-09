# 3607
'''
def F(n):
    if n > 50:
        return 0
    elif n == 50:
        return 1
    else:
        return F(n+2) + F(n*5)
print(F(2))
'''

# 11358
'''
def F(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x + 1, y) + F(x + 2, y) + F(x * 2, y)
print(F(3, 10) * F(10, 12))
'''

# 13418
'''
def F(x, y):
    if x > y or x == 26:
        return 0
    elif x == y:
        return 1
    else:
        return F(x + 1, y) + F(2*x + 1, y)

print(F(1, 27))
'''
#15144

'''def f(x,y):
    if x > y or x == 14:
        return 0
    elif x == y:
        return 1
    else:
        return f(x+2,y) + f(x+1,y)

print(f(2,9) * f(9,18))'''

#15638

'''def f(x,y):
    if x > y or x == 17:
        return 0
    elif x == y:
        return 1
    else:
        return f(x+1,y) + f(x*2,y)

print(f(1,10) *f(10,21))'''


#15807

'''def f(x,y):
    if x > y or x == 33:
        return 0
    elif x == y:
        return 1
    else:
        return f(x+1,y) + f(x*2,y)

print(f(3,16) * f(16,37))'''

#15834

'''def f(x,y):
    if x > y or x == 31:
        return 0
    elif x == y:
        return 1
    else:
        return f(x+1,y) + f(x*2,y)

print(f(2,15) * f(15,35))'''

'''def f(x,y):
    if x > y or x==16:
        return 0
    elif x == y:
        return 1
    else:
        return f(x+1,y) + f(x*2,y)

print(f(1,10) * f(10,21))'''

#72581
'''
def f(x,y):
    if x < y:
        return 0
    elif x == y:
        return 1
    else:
        return f(x-2,y) + f(x//2,y) + f(x//3,y)

print(f(40,20)*f(20,4))
'''

# 46981
'''def f(x, y, Flag):
    if x > y:
        return 0
    if x == y:
        return 1
    elif Flag:
        return f(x + 1, y, True) + f(x + 2, y, True) + f(x * 2, y, False)
    else:
        return f(x + 1, y, True) + f(x + 2, y, True)

print(f(1, 11, True))'''

#52194
def f(x,y,Flag, Flag2):
    if x > y:
        return 0
    elif x == y:
        return 1
    elif x < y:
        if Flag == False and Flag2 == True:
            return f(x*2,y,True, False)
        elif Flag2 == False and Flag == True:
            return f(x+1,y,False,True)
        else:
            return f(x+1, y, False,True) + f(x*2,y, True,False)
print(f(1,16,True,True))