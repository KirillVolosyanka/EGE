f = open('37336.txt')
lines = [int(i) for i in f]
result = []
for i in range(len(lines) - 1):
    if (lines[i] % 3 == 0) or (lines[i+1] % 3 == 0):
        result.append(lines[i] + lines[i+1])
print(len(result), max(result))