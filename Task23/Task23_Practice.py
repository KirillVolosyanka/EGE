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

