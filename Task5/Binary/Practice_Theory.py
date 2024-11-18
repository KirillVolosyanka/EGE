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
