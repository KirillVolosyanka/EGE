# 45250
'''
def F(n):
    if n < 3:
        return 2
    elif n % 2 == 0:
        return F(n - 2) + F(n - 1) - n
    else:
        return F(n - 1) - F(n - 2) + 2 * n

print(F(32))
'''

# 47220
slovar = {1 : 1}
for i in range(2, 2024):
    slovar[i] = i * slovar[i - 1]
print(slovar[2023] / slovar[2020])

# Example
'''
slovar = {1: 12}
slovar["Vasya"] = "Shpala"
slovar.pop("Vasya")
slovar["Vasya"] = "Tuneyadec"
slovar["Vasya"] = "Chmo"
print(slovar.keys())
'''

#36871
'''def f(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return f(n/2)
    else:
        return 1+f(n-1)

count = 0

for i in range(1,1001):
    if f(i) == 3:
        count+=1
print(count)
'''

#38591

'''def f(n):
    if n ==1:
        return 1
    elif n % 2 == 0:
        return n + f(n-1)
    elif n >1 and n%2==1:
        return 2*f(n-2)

print(f(26))'''

#



