# 9365
x = '8' * 68
while (('222' in x) or ('888' in x)):
    if '222' in x:
        x = x.replace('222', '8', 1)
    else:
        x = x.replace('888', '2', 1)

print(x)