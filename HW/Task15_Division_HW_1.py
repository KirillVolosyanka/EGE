# Number 1

'''def t(n,m, k):
    return max(n,m,k) < n + m + k - max(n,m,k)
def f(A,x):
    return not(t(x,10,20)) or (not((max(x,8) > 24)) == (not t(3,A,x)))

for a in range(1,100):
    ok = True
    for x in range(1,500):
        #((ТРЕУГ(X,10,20) → (¬(МАКС(X, 8) > 24))) = ¬(ТРЕУГ(3,A, X)))
        if f(a, x) == False:
            ok = False
            break
    if ok:
        print(a)'''


# Answer: _ _ _ _

'''_________________________________________________________________________'''

# Number 2
'''for a in range(1,1000):
    ok = True
    for x in range(1,1000):
        if ((( x %2 != 0) or (x % 3 != 0)) or (x + a >= 100)) == False:
            ok = False
            break
    if ok:
        print(a)
        break'''
# Answer: 94

'''_________________________________________________________________________'''

# Number 3
'''for a in range(1,500):
    ok = True
    for x in range(1,500):
        if (((72 % x != 0) or (120 % x !=0)) or (a - x > 100)) == False:
            ok = False
            break
    if ok:
        print(a)
        break'''
# Answer: 125

'''_________________________________________________________________________'''

# Number 4
#(A < 50) ∧ (¬ДЕЛ(X, А) → (ДЕЛ(X, 10) → ¬ДЕЛ(X, 18)))

'''for a in range(1,500):
    ok = True
    for x in range(1,500):
        if ((a <50) and ((x%a==0) or ((x%10!=0) or (x%18!=0)))) == False:
            ok = False
            break
    if ok:
        print(a)'''


# Answer: 45

'''_________________________________________________________________________'''

# Number 5
'''b = list(range(70,91))
for a in range(1,1000):
    ok = True
    for x in range(1,1000):
        if ((x % a == 0) or (not(x in b) or ( x % 22 != 0))) == False:
            ok = False
            break

    if ok:
        print(a)'''

# Answer: 88

# Number 6
#ДЕЛ(X, А) → (ДЕЛ(X, 21) + ДЕЛ(X, 35))

'''for a in range(1,500):
    ok = True
    for x in range(1,500):
        if ((x%a!=0) or ((x%21==0) + (x%35==0))) == False:
            ok = False
    if ok:
        print(a)
        break'''
# Answer: 21

'''_________________________________________________________________________'''

# Number 7
def f(a,b,c):
    if (a+b>c) and (a+c>b) and (b+c>a):
        return True
    else: return False

for a in range(1,500):
    ok = True
    for x in range(1,500):

#        ¬((ТРЕУГ(Х, 11, 16) ≡ (¬(МАКС(X, 5) > 10))) ∧ ТРЕУГ(4, A, X))
        if (not((f(x,11,16) == (not(max(x,5) > 10))) and f(4,a,x))) == False:
            ok = False
            break
    if ok:
        print(a)

# Answer: _ _ _ _
