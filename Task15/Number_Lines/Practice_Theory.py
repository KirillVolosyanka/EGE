# 7763
'''
answer = []
P = [i for i in range(5, 30)]
Q = [i for i in range(14, 23)]
for A_down in range(1, 101):
    for A_up in range(A_down + 1, 101):
        Ok = True
        A = [i for i in range(A_down, A_up)]
        for x in range(-500, 500):
            f = not((x in P) == (x in Q)) or (not(x in A))
            if f == False:
                Ok = False
                break
        if Ok:
            answer.append(A_up - A_down)
print(max(answer))
'''

# 8666 Vasya

'''res = []
P = [i for i in range(25, 50)]
Q = [i for i in range(32, 47)]

for A_down in range (1, 51):
    for A_up in range(A_down + 1, 51):
        ok = True
        A = [i for i in range(A_down, A_up)]
        for x in range(-500, 500):
            f = not((x in A) or (x in P)) or (not(x in A) or (x in Q))
            if f == False:
                ok = False
                break
        if ok:
            res.append(A_up - A_down)
print(max(res))
'''
# 8666
'''
answer = []
P = [i for i in range(25, 50)]
Q = [i for i in range(32, 47)]
for A_down in range(0, 60):
    for A_up in range(A_down + 1, 60):
        Ok = True
        A = [i for i in range(A_down, A_up)]
        for x in range(-500, 500):
            f = (not((x in A) or (x in P))) or (not(x in A) or (x in Q))
            if f == False:
                Ok = False
                break
        if Ok:
            answer.append(A_up - A_down)
print(max(answer))
'''

# 9653
'''
answer = []
P = [i for i in range(10, 29)]
Q = [i for i in range(13, 19)]
for A_down in range(0, 60):
    for A_up in range(A_down + 1, 60):
        Ok = True
        A = [i for i in range(A_down, A_up)]
        for x in range(-500, 500):
            f = (not(x in A) or (x in P)) or (x in Q)
            if f == False:
                Ok = False
                break
        if Ok:
            answer.append(A_up - A_down)
print(max(answer))
'''
'''res = []
P = [i for i in range(10, 29)]
Q = [i for i in range(13, 18)]

for A_down in range(10, 30):
    for A_up in range(A_down + 1, 30):
        ok = True
        A = [i for i in range(A_down, A_up)]
        for x in range(-700,700):
            f = (not(x in A) or (x in P)) or (x in Q)
            if f == False:
                ok = False
                break
        if f == True:
            res.append(A_up - A_down)
print(max(res))
'''
# 9699
'''
answer = []
P = [i for i in range(4, 15)]
Q = [i for i in range(12, 20)]
for A_down in range(4, 21):
    for A_up in range(A_down + 1, 21):
        Ok = True
        A = [i for i in range(A_down, A_up)]
        for x in range(-500, 500):
            f = not((x in P) and (x in Q)) or (x in A)
            if f == False:
                Ok = False
                break
        if Ok:
            answer.append(A_up - A_down)
print(min(answer))
'''

'''res = []
P = [i for i in range(4, 15)]
Q = [i for i in range(12, 20)]

for A_down in range(4, 21):
    for A_up in range(A_down + 1, 21):
        ok = True
        A = [i for i in range(A_down, A_up)]
        for x in range (-500, 500):
            f = not((x in P) and (x in Q)) or (x in A)
            if f == False:
                ok = False
                break
        if ok == True:
            res.append(A_up - A_down)

print(max(res))'''
'''num = []
p = [i for i in range(15,40)]
q = [i for i in range(21,63)]

for a_down in range(15,64):
    for a_up in range(a_down + 1,64):
        ok = True
        a = [i for i in range(a_down,a_up)]
        for x in range(-1000,1000):
            if (not(x in p) or not(((x in q) and not(x in a)) or not(x in p))) == False:
                ok = False
                break
        if ok:
            num.append(a_up-a_down)

print(min(num))'''

#17336
'''for a in range(0,1000):
    ok = True
    for x in range(0,1000):
        for y in range(0,1000):
            if ((3*x + 4*y !=60) or ((a >= x) and (a >= y))) == False:
                ok = False
                break
    if ok:
        print(a)'''

'''for a in range(-500,500):
    ok = True
    for x in range(1,500):
        for y in range(1,500):
            if (((108 % x != 0) or (x % y !=0)) or (x + y > 80) or (a - y > x)) == False:
                ok = False
                break
    if ok:
        print(a)'''

#55811

'''for a in range(0,500):
    ok = True
    for x in range(0,500):
        if (x&39 == 0 or (not(x&11 ==0) or (x&a != 0) )) == False:
            ok = False
            break
    if ok:
        print(a)'''

#35989

for a in range(0,500):
    ok = True
    for x in range(0,500):
        if ((x&73 != 0) or ((x&28 == 0) or (x&a!=0))) == False:
            ok = False
            break
    if ok:
        print(a)




