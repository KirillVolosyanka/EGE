'''a = open('24.txt').read().split("D")
maxL = []

for i in range(len(a)):

    if a[i].count("O") <= 2:
        maxL.append(len(a[i])+2)
        print(a[i])

print(max(maxL))


s = open('24.txt').read().split('D')[1:-1]
mx = 0
c = 1 # =1 так, как цепочка должна начинаться с D
for i in range(len(s)):
    if s[i].count('O') <= 2:
        c += len(s[i]) + 1 #+1 так, как цепочка должна заканчиваться D
        mx = max(mx, c)
    else:
        c = 1
print(mx)'''


#24.2

'''a = open("24 (1).txt").read()
numLen = []
for i in range(len(a)):
    cA = 0
    cB = 0
    lenLine = 0
    for j in range(i,len(a)):
        lenLine+=1
        if a[j] == "A":
            cA+=1
        if a[j] == "B":
            cB +=1
        if cA > 1 or cB > 1:
            break
    numLen.append(lenLine-1)

print(max(numLen))'''

#29672
'''a = open("inf_22_10_20_24.txt").readlines()
c = 0
for line in a:


    print(line)
    cA = line.count("A")
    cE = line.count("E")
    if cE > cA:
        c+=1

print(c)'''

#19149
'''a = open("24_19149.txt").readline().split('(')'''

#58532

'''f = open("24 (3).txt").readline()
keyCoo = [-3]
maxLen = 0
pat = "XYZ_XZY_ZXY_YZX_YXZ_ZYX"

for i in range(len(f)-2):
    a = f[i]
    b = f[i+1]
    c = f[i+2]

    if a+b+c in pat:
        keyCoo.append(i)


keyCoo.append(len(keyCoo))

for j in range(len(keyCoo)-1):
    curLen = keyCoo[j+1] - keyCoo[j] - 3
    if curLen > maxLen:
        maxLen = curLen

print(maxLen)'''

#63040
'''f = open("24 (4).txt").readline()


maxLen = 0
curLen = 0

for i in range(len(f)):
    cA = 0
    cB = 0

    for j in range(i,len(f)):
        if f[j] == "A": cA += 1
        elif f[j] == "B": cB += 1

        if cA > 2 or cB > 2: break
        else: curLen+=1

    if curLen > maxLen:
        maxLen = curLen
    curLen = 0

print(maxLen)'''

#58327

f = open("24_58327.txt").readline()

maxLen = 1
curLen = 1

for i in range(len(f)):

    if f[i-1] >= f[i]:
        curLen +=1

    else:
        if curLen > maxLen:
            maxLen = curLen
        curLen = 1

print(maxLen)

























