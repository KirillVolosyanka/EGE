# 27774
'''
1. -1 or /2
2. In the first 10 stones
3. End - sum of two group = 20 or less
'''

def f(x, y, h):
    if h == 3 and x + y <= 20:
        return 1
    elif h == 3 and x + y > 20:
        return 0
    elif x + y <= 20 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x - 1, y, h + 1) or f(x, y - 1, h + 1) or f(x // 2 + x % 2, y, h + 1) or f(x, y // 2 + y % 2, h + 1)  # стратегия победителя
        else:
            return f(x - 1, y, h + 1) or f(x, y - 1, h + 1) or f(x // 2 + x % 2, y, h + 1) or f(x, y // 2 + y % 2, h + 1)  # стратегия проигравшего(неудачный ход)

for x in range(100, 10, -1):
    if f(x, 10, 1) == 1:
        print("Задача 19:", x)
        break

# -------------

def f(x, y, h):
    if h == 4 and x + y <= 20:
        return 1
    elif h == 4 and x + y > 20:
        return 0
    elif x + y <= 20 and h < 4:
        return 0
    else:
        if h % 2 != 0:
            return f(x - 1, y, h + 1) or f(x, y - 1, h + 1) or f(x // 2 + x % 2, y, h + 1) or f(x, y // 2 + y % 2, h + 1)   # стратегия победителя
        else:
            return f(x - 1, y, h + 1) and f(x, y - 1, h + 1) and f(x // 2 + x % 2, y, h + 1) and f(x, y // 2 + y % 2, h + 1)  # стратегия проигравшего(любой ход)

for x in range(10, 1000):
    if f(x, 10, 1) == 1:
        print("Задача 20:", x)

# --------

def f(x, y, h):
    if (h == 3 or h == 5) and x + y <= 20:
        return 1
    elif h == 5 and x + y > 20:
        return 0
    elif x + y <= 20 and h < 5:
        return 0
    else:
        if h % 2 == 0:
            return f(x - 1, y, h + 1) or f(x, y - 1, h + 1) or f(x // 2 + x % 2, y, h + 1) or f(x, y // 2 + y % 2, h + 1)  # стратегия победителя
        else:
            return f(x - 1, y, h + 1) and f(x, y - 1, h + 1) and f(x // 2 + x % 2, y, h + 1) and f(x, y // 2 + y % 2, h + 1)  # стратегия проигравшего(любой ход)

def f1(x, y, h):
    if h == 3 and x + y <= 20:
        return 1
    elif h == 3 and x + y > 20:
        return 0
    elif x + y <= 20 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f1(x - 1, y, h + 1) or f1(x, y - 1, h + 1) or f1(x // 2 + x % 2, y, h + 1) or f1(x, y // 2 + y % 2, h + 1)  # стратегия победителя
        else:
            return f1(x - 1, y, h + 1) and f1(x, y - 1, h + 1) and f1(x // 2 + x % 2, y, h + 1) and f1(x, y // 2 + y % 2, h + 1)  # стратегия проигравшего(любой ход)

for x in range(10, 100):
    if f(x, 10, 1) == 1:
        print(x)
print("====")
for x in range(10, 100):
    if f1(x, 10, 1) == 1:
        print(x)