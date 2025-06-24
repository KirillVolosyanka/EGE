#19.2
def f(x,h):
    if 20 <= x <= 30 and h == 3:
        return 1
    if 20 <= x <= 30 and h > 3:
        return 0
    if h == 3 and (x < 20 or x > 30):
        return 0
    if h < 3 and 20 <= x <= 30:
        return 0
    else:
        if h % 2 == 0:
            return f(x+1,h+1) or f(x*2,h+1)
        else:
            return f(x+1,h+1) or f(x*2,h+1)

for x in range(1,20):
    if f(x,1):
        print(x)

#19.1
def f(x,h):
    if h == 3 and x >= 129:
        return 1
    if h == 3 and x < 129:
        return 0
    if h < 3 and x >= 129:
        return 0
    else:
        if h % 2 == 0:
            return f(x+1,h+1) or f(x*2,h+1)
        else:
            return f(x+1,h+1) and f(x*2,h+1)

for x in range(1,129):
    if f(x,1):
        print(x)

#20.1
def f(x,h):
    if h == 4 and x >= 129:
        return 1
    if h == 4 and x < 129:
        return 0
    if h < 4 and x >= 129:
        return 0
    else:
        if h % 2 != 0:
            return f(x+1,h+1) or f(x*2,h+1)
        else:
            return f(x+1,h+1) and f(x*2,h+1)

for x in range(1,129):
    if f(x,1):
        print(x)

#21.1
def fs(x,h):
    if h == 3 and x >= 129:
        return 1
    if h == 3 and x < 129:
        return 0
    if h < 3 and x >= 129:
        return 0
    else:
        if h % 2 == 0:
            return fs(x + 1, h + 1) or fs(x * 2, h + 1)
        else:
            return fs(x + 1, h + 1) and fs(x * 2, h + 1)

def f(x,h):
    if (h == 3 or h == 5) and x >= 129:
        return 1
    if h == 5 and x < 129:
        return 0
    if h < 5 and x >= 129:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x * 2, h + 1)
        else:
            return f(x + 1, h + 1) and f(x * 2, h + 1)

for x in range(1,129):
    if (f(x,1) == True) and (fs(x,1) == False):
        print(x)