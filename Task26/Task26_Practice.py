#29674
'''a = open("inf_22_10_20_26.txt")
data = int(a.readline())
stock = sorted([int(i) for i in a])
mt50 = []
lt50 = []
total = 0
for i in range(len(stock)):
    if stock[i] >= 50:
        mt50.append(stock[i])
    else:
        lt50.append(stock[i])

sorted(mt50)
midL = len(mt50)//2

total += sum(lt50)

res = []
for i in range(midL):
    total += mt50[i]*0.75
    res.append(mt50[i])

for i in range(midL,len(mt50)):
    total += mt50[i]

print(total,max(res))'''

#33198

a = open("26 (1).txt")
data = a.readline()
stock = [int(i) for i in a]
dron = []
mefe = []
stopNarcotics = []
for i in range(len(stock)):
    if 200 <= stock[i] <= 210:
        dron.append(stock[i])
    else: mefe.append(stock[i])

mefe = sorted(mefe)
Nomefedron = 10000 - sum(dron)
totalMefedron = []

for j in range(len(mefe)):
    if sum(totalMefedron) + mefe[j] <= Nomefedron:
        totalMefedron.append(mefe[j])
    else: print(len(totalMefedron) + len(dron),sum(totalMefedron) + sum(dron))

print(9963 - totalMefedron[-3] + 159)









