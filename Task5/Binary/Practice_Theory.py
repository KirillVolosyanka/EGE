# 8094
def add(x):
    x = str(x)
    if x.count('1') % 2 == 0:
        x += '0'
    else:
        x += '1'
    return x

for i in range(1, 500):
    bin_N = bin(i)
    bin_N = str(bin_N)[2:]
    bin_N = add(bin_N)
    bin_N = add(bin_N)
    dec_N = int(bin_N, 2)
    if dec_N > 43:
        print(dec_N)

# MISIS
for n in range(1000):
    s = bin(n)[2::][::-1]
    s = int(s, 2)
    if s == 23:
        print(n)

#MISIS
MaxR = []
for n in range(12 + 1):
    R = bin(n)[2::]

    if n % 2 == 0:
      R = "10" + R

    else:
      R = "1" + R + "01"

    R = int(R,2)
    MaxR.append(n)
print(max(MaxR))

#MISIS

MinN = []
for n in range (0, 100):
    R = bin(n)[2:]
    if n % 2 == 0:
      R = R + "01"

    else:
      R = R + "10"
    if int (R,2) > 138:
        MinN.append(n)
print(min(MinN))