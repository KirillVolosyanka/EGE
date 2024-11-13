# Number 1
'''res = []
p = [ i for i in range(24,77)]
q = [ i for i in range(47,92)]
r = [i for i in range(82,116)]

for A_down in range(24,117):
    for A_up in range(A_down + 1, 117):
        ok = True
        a = [ i for i in range(A_down, A_up)]
        for x in range(-500, 500):
            if (not(not(not(x in q)or((x in p)or(x in r))))or((x in a) or not(x in q))) == False:
                ok = False
                break
        if ok:
            res.append(A_up - A_down)

print(min(res))'''
from operator import truediv

# Answer: 5

'''_________________________________________________________________________'''

# Number 2
'''res = []
P = [i for i in range(20,50)]
Q = [i for i in range(30,65)]

for A_down in range(20, 66):
    for A_up in range(A_down + 1, 66):
        ok = True
        A = [i for i in range(A_down, A_up)]
        for X in range(-500,500):
            if ((X in A) or (not(X in P) or not(X in Q))) == False:
                ok = False
                break
        if ok:
            res.append(A_up - A_down)
print(min(res))
'''
# Answer: 20

'''_________________________________________________________________________'''

# Number 3
'''
    res = []
P = [i for i in range(5, 30)]
Q = [i for i in range(14,23)]

for A_down in range(5,31):
    for A_up in range(5,31):
        ok = True
        A = [i for i in range(A_down, A_up)]
        for X in range(-500,500):
            if (not((X in P) == (X in Q)) or not(X in A)) == False:
                ok = False
                break
        if ok:
            res.append(A_up - A_down)

print(max(res))

'''

# Answer: 9

'''_________________________________________________________________________'''

# Number 4
'''
    res = []
P = [ i for i in range(23,58)]
Q = [ i for i in range(1,39)]

for A_down in range(1, 59):
    for A_up in range(A_down + 1, 59):
        ok = True
        A = [i for i in range(A_down, A_up)]
        for X in range(-2000,2000):
            if (not((X in P)or (X in A)) or ((X in Q) or (X in A))) == False:
                ok = False
                break
        if ok:
            res.append(A_up - A_down)
print(min(res))
'''

# Answer: 19

'''_________________________________________________________________________'''

# Number 5
'''res = []
P = [i for i in range(10,40)]
Q = [i for i in  range(5,15)]
R = [i for i in range(35,50)]

for A_down in range(5,51):
    for A_up in range(A_down + 1,51):
        ok = True
        A = [i for i in range(A_down, A_up)]
        for X in range(-500,500):
            if (((X in A) or (X in P) ) or (not(X in Q) or (X in R))) == False:
                ok = False
                break
        if ok:
            res.append(A_up - A_down)
print(min(res))'''

# Answer: 5