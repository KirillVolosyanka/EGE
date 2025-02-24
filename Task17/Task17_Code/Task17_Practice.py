
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

file = open("61363.txt")
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

print(len(res),max(res))


