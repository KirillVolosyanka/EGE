# Number 1
'''res = []
P = [ i for i in range(24,77)]
Q = [ i for i in range(47,92)]
R = [ i for i in range(82,116)]

for A_down in range(24,117):
    for A_up in range(A_down +1, 117):
        ok = True
        A = [i for i in range (A_down, A_up)]
        for X in range(-500,500):
            if (not(not(not(X in Q) or ((X in  P) or (X in R)))) or ((X in A) or not(X in Q))) == False:
                ok = False
        if ok:
            res.append(A_up - A_down)
print(min(res))'''

# Answer: 5

'''_________________________________________________________________________'''

# Number 2
'''res = []
P = [i for i in range(20,50)]
Q =[ i for i in range(30,65)]

for A_down in range(20,66):
    for A_up in range(A_down + 1,66):
        ok = True
        A = [i for i in range(A_down, A_up)]
        for X in range(-1000,1000):
            if ((X in A) or (not(X in P) or not(X in Q))) == False:
                ok = False
        if ok:
            res.append(A_up - A_down)
print(min(res))'''
# Answer: 20


# Number 3
'''res = []
P= [i for i in range(5, 30)]
Q = [i for i in range(14, 23)]

for A_down in range(5,31):
    for A_up in range(A_down +1,31):
        ok = True
        A = [i for i in range(A_down,A_up)]
        for X in range(-500,500):
            if (not((X in P) == (X in Q)) or not(X in A)) == False:
                ok = False
        if ok:
            res.append(A_up - A_down)
print(max(res))'''

# Answer: 9



# Number 4
'''res = []
P = [i for i in range(23, 58)]
Q = [i for i in range(1, 39)]

for A_down in range(1,59):
    for A_up in range(A_down + 1,59):
        ok = True
        A = [i for i in range(A_down, A_up)]
        for X in range(-500,500):
            if (not((X in P) or (X in A)) or ((X in Q) or (X in A))) == False:
                ok = False
        if ok:
            res.append(A_up - A_down)

print(min(res))'''
# Answer: 19

'''_________________________________________________________________________'''

# Number 5
res = []
P = [i for i in range(10, 40)]
Q = [i for i in range(5, 15)]
R = [i for i in range(35, 50)]

for A_down in range(5,51):
    for A_up in range(A_down + 1,51):
        ok = True
        A = [i for i in range(A_down, A_up)]
        for X in range(-500,500):
            if (((X in A) or (X in P)) or (not(X in Q) or (X in R))) == False:
                ok = False
        if ok:
            res.append(A_up - A_down)
print(min(res))
# Answer: 5