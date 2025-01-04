# Number 1
'''start = 81**15 + 3 ** 22 - 27
print(start)
def conv(n,sys):
    res = ''
    while n != 0:
        res =str (n % sys) +res
        n//sys
    return res

res = conv(start,9)
res = res.count("8")
print(res)'''

# Answer: _ _ _ _

'''_________________________________________________________________________'''

# Number 2
'''for x in "0123456789":
    x1 = str(x) + "B09"
    x2 = str(x) + "8E8"
    res = int(x1,17) + int (x2,15)
    if res % 155 == 0:
        res = res // 155
        print(res)'''

# Answer: 194

'''_________________________________________________________________________'''

# Number 3
'''d1 = 1*37**7 + 2*37**6 + 6*37**4 + 4*37**3 + 3*37**2 + 7
c = []
for x in range(1,37):
    for y in range(1,37):
        d = d1 + x*37**5 + y*37**1
        if d % 36 == 0:
            c.append(y*37**1 + x)
print(max(c))'''
# Answer: 1345


# Number 4
'''for x in '0123456789ABCDE':
    for y in '0123456789ABCDE':
        x1 = '90' + str(x) + '4' + str(y)
        x2 = '91' + str(x) + str(y) + '2'
        res = int(x1, 15) + int (x2,16)
        if res % 56 ==0:
            res = res // 56
            print(res)
            break'''
# Answer: 18754

'''_________________________________________________________________________'''
        
# Number 5

'''def conv(n,r):
    ans = ''
    while n:
        ans = str(n % r) + ans
        n //= r
    return ans

s = []

for x in range(1,2031):
    d = 7**170 + 7**100 - x
    d = str(conv(d,7))
    count = d.count("0")

    if count == 71:
        s.append(x)
print(max(s))'''
# Answer: 2029

# Number 6
'''for x in '0123456789ABCDEF':
    d1= "2" + str(x) + "84"
    d2 ="2B3" + str(x)
    res = int(d1,19) + int(d2,16)

    if res % 88 == 0:
        print(res//88)'''

# Answer: 345

'''_________________________________________________________________________'''

# Number 7

'''for x in '0123456789ABCDEFGHIJKLMNOPQRSTU':
    d1 = '123' + str(x) + 'AB3'
    d2 = '3CE' + str(x) + '321'
    res = int(d1,31) + int(d2,31)

    if res % 17 == 0:
        print(res//17)'''
# Answer: 233409739

'''_________________________________________________________________________'''

# Number 8
for x in '0123456789AB':
    for y in '0123456789AB':
        d1 = str(x) + '231' + str(y)
        d2 = '78' + str(x) +'98'+ str(y)
        res = int(d1,12) + int(d2,14)
        if res % 99 == 0:
            print(res//99)


# Answer: 41428

'''_________________________________________________________________________'''

# Number 9
print(bin(16**5 + 8**6 + 4**9 - 128).count("1"))
# Answer: 13

'''_________________________________________________________________________'''

# Number 10


'''for x in range(0,38):
    d1 = 15 * 37 ** 8 + 2 * 37 ** 7 + 9 * 37 ** 6 + x + 8 * 37 ** 4 + 14 * 37 ** 3 + 10 * 37 ** 2 + 13 * 37 ** 1 + 6
    d2 = 11 * 37 ** 8 + 10 * 37 ** 7 + x + 13 * 37 ** 5 + 14 * 37 ** 4 + 0 * 37 ** 3 + 12 * 37 ** 2 + 1 * 37 ** 1 + 11
    res = d1 * d2

    if res % 36 == 0:
        d1 = 1*37**2 + x*37**1 + 2
        print(d1)'''

# Answer: 2703


