
'''f = open('37336.txt')
lines = [int(i) for i in f]
result = []
for i in range(len(lines) - 1):
    if (lines[i] % 3 == 0) or (lines[i+1] % 3 == 0):
        result.append(lines[i] + lines[i+1])
print(len(result), max(result))'''

'''f = open("37337.txt")
lines = [int(i) for i in f]
res = []

for i in range(len(lines)):
    for j in range(i, len(lines)):
        if i != j:
            if lines[i] % 160 != lines[j] % 160:
                if lines[i] % 7 == 0 or lines[j] % 7 == 0:
                    res.append(i + j)

print(max(res),len(res))'''

'''file = open("39763.txt")
lines = [int(i) for i in file]

num = []
countTr = 0

for i in range(len(lines)-2):
    
    a = min(lines[i],lines[i+1],lines[i+2])
    c = max(lines[i],lines[i+1],lines[i+2])
    b = (lines[i] + lines[i+1] + lines[i+2]) - a - c

    if c**2 < a**2 + b**2 and min(a,b,c) != 0:
        countTr+=1
        num.append(a+b+c)


print(countTr,max(num))'''
'''file = open("61363.txt")
lines = [int(i) for i in file]
max19 =[]
for i in range(len(lines)):
    if lines[i] % 100 == 19:
        max19.append(lines[i])

maxN19 = max(max19)

res = []
for i in range(len(lines)-2):
    a = lines[i]
    b = lines[i+1]
    c = lines[i+2]

    if ((len(str(a)) == 4 and len(str(b)) == 4) or (len(str(b)) == 4 and len(str(c)) == 4) or
        (len(str(c)) == 4 and len(str(a)) == 4)):
        print("ip")
        if (a % 3 == 0 or b % 3 == 0 or c % 3 == 0) and (a+b+c) > maxN19:
            res.append((a+b+c))
            print("io2")

print(len(res),max(res))'''

#59785

'''aa = open("17 (2).txt")
data = [int(i) for i in aa]
l = sorted(data)
m13 = 0
sums = []

for i in range(len(data)-1,0,-1):
    if l[i] % 100 == 13:
        m13 = l[i]
        break

for j in range(len(data) - 2):
    a = data[j]
    b = data[j+1]
    c = data[j+2]
    sum = a + b + c
    if sum <= m13:
        if (len(str(abs(a))) == 3 and len(str(abs(b))) == 3 and len(str(abs(c))) != 3) or (len(str(abs(c))) == 3 and len(str(abs(b))) == 3 and len(str(abs(a))) != 3) or (len(str(abs(a))) == 3 and len(str(abs(c))) == 3 and len(str(abs(b))) != 3):
            sums.append(sum)


print(len(sums),min(sums))'''


'''a = open("17 (3).txt")
data = [int(i) for i in a]
sumAB = []
for i in range(len(data)-1):
    for j in range(i+1,len(data)):
        a = data[i]
        b = data[j]
        if a % 7 == 0 or b % 7 ==0:
            if a % 160 != b % 160:
                sumAB.append(a+b)

print(len(sumAB), max(sumAB))
'''

'''a = open("17 (4).txt")
data = [int(i) for i in a]
lastMax = max(data) % 10
lastMin = min(data) % 10
sumABC = []
for i in range(len(data)-2):
    a = data[i]
    b = data[i+1]
    c = data[i+2]

    if (len(str(abs(a))) == 5 and len(str(abs(b))) != 5 and len(str(abs(c))) != 5) or (len(str(abs(b))) == 5 and len(str(abs(a))) != 5 and len(str(abs(c))) != 5) or (len(str(abs(c))) == 5 and len(str(abs(b))) != 5 and len(str(abs(a))) != 5):
        if a % 10 == lastMin or b % 10 == lastMin or c % 10 == lastMin:
            if a % 10 != lastMax and b % 10 != lastMax and c % 10 != lastMax:
                sumABC.append(a+b+c)


print(len(sumABC), max(sumABC))'''

'''a = open("17 (6).txt")
data = [int(i) for i in a]

shtSum = []
for i in range(len(data)-2):
    a = data[i]
    b = data[i+1]
    c = data[i+2]

    if a > 0 and b > 0 and c > 0:

        if max(a,b,c)**2 == min(a,b,c)**2 + (a+b+c-max(a,b,c)- min(a,b,c))**2:
            print("io")

print(len(shtSum))'''

'''a = open("17 (7).txt")
data = [int(i) for i in a]
res = []
for i in range(len(data)):
    for j in range(i+1, len(data)-1):
        a = data[i]
        b = data[j]

        if abs(a-b) % 36 == 0 and (a % 13 == 0 or b % 13 == 0):
            res.append(abs(a-b))
print(len(res),max(res))'''