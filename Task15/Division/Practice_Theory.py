# 8106
'''for A in range(1, 100):
    Ok = True
    for x in range(1, 1000):
        F = (x % A == 0) or ((x % 6 != 0) or (x % 4 != 0))
        if F == False:
            Ok = False
            break
    if Ok:
        print(A)
'''

#27412

'''for A in range (1, 100):
    ok = True
    for x in range (1,100):
        f = (x % A == 0) or (x % 6 != 0) or (x % 9 !=0)
        if f == 0:
            ok = False
            break
    if ok == True:
        print(A)
'''

#

for A in range (1, 100):
    ok = True
    for x in range (1, 100):
        f = (A < 50) and ((x % A == 0) or ((x % 10 != 0) or (x % 12 != 0)))
        if f == False:
            ok = False
    if ok == True:
        print(A)

