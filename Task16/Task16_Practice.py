# 45250
'''
def F(n):
    if n < 3:
        return 2
    if n % 2 == 0 and n > 2:
        return F(n - 2) + F(n - 1) - n
    if n % 2 != 0 and n > 2:
        return F(n - 1) - F(n - 2) + 2 * n
print(F(32))
'''

# 47220
'''
slovar = {1 : 1}
for i in range(2, 2024):
    slovar[i] = i * slovar[i - 1]
print(slovar[2023] / slovar[2020])
'''

# Example
'''
slovar = {}
slovar["Vasya"] = "Shpala"
slovar.pop("Vasya")
slovar["Vasya"] = "Tuneyadec"
print(slovar.keys())
'''