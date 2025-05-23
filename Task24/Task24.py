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
a = open("24_19149.txt").readline().split('(')


