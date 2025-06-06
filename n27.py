a = open("inf_26_04_21_27b.txt").readlines()
data = []
for line in a:
    line = line.split()
    line = [int(i) for i in line]
    if line[1] % 2 != 0:
        data.append((line[0],line[1]))

sumMin = 0
sumMax = 0
for i in range(len(data)):
    sumMin += min(data[i])
    sumMax += max(data[i])
print(sumMin,sumMax)
minSumCheck = 980808347
sumMaxMin = sumMin + sumMax
for j in range(len(data)):
    sumMX = min(data[j]) + max(data[j])
    if min(data[j]) % 2 != 0 and max(data[j]) % 2 != 0:
        if sumMX < minSumCheck:
            minSumCheck = sumMX

print(sumMaxMin - minSumCheck)