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

res = []
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

print(max(res))