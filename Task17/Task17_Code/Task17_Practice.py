
'''f = open('37336.txt')
lines = [int(i) for i in f]
result = []
for i in range(len(lines) - 1):
    if (lines[i] % 3 == 0) or (lines[i+1] % 3 == 0):
        result.append(lines[i] + lines[i+1])
print(len(result), max(result))'''

f = open("37337.txt")
lines = [int(i) for i in f]
res = []

for i in range(len(lines)):
    for j in range(i, len(lines)):
        if i != j:
            if lines[i] % 160 != lines[j] % 160:
                if lines[i] % 7 == 0 or lines[j] % 7 == 0:
                    res.append(i + j)

print(max(res),len(res))
