# 8094
'''def add(x):
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
        print(dec_N)'''
#15622

'''MinR =[]

for i in range(1, 500):
    r = str(bin(i)[2:])
    if r.count("1") % 2 == 0:
        r = r + "00"
    else:
        r = r + "11"
    r = int(r, 2)
    if r > 114:
        MinR.append(r)
print(min(MinR))'''