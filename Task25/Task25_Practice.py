#45259
'''
for num in range(0, 10**9, 23):
    num_line = str(num)
    if num_line[0] == "1" and num_line[1] == "2" and num_line[2] == "3" and num_line[3] == "4" and num_line[4] == "5" and num_line[-3] == "7" and num_line[-1] == "8":
        print(num, num / 23)'''

#47229

'''for num in range(0, 10**10, 2023):
    num_line = str(num)
    if num_line[0] == "1" and num_line[2] == "2" and num_line[3] == "1" 
        and num_line[4] == "3" and num_line[5] == "9" and num_line[-1] == "4":
        print(num, num / 2023)'''

#48446

'''for num in range(0,10**10,2023):
    num_line = str(num)
#1?493*41
    if (num_line[0] == "1" and num_line[2:5] == "493"
            and num_line[-2] == "4" and num_line[-1] == "1"):
        print(num)'''

#48473
#1?954*21

'''for num in range(0,10**10,3023):
    num_line = str(num)

    if num_line[0] == "1" and num_line[2:5] == "954" and num_line[-2] == "2" and num_line[-1] == "1":
        print(num)'''

#59818
#соответствуют маске *31*65?;
#делятся на 31 и 2031 без остатка;

'''def F(num):
    dvoika = []
    for i in range(0, 20):
        dvoika.append(2**i)
    c = 1
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            c += 1
    if dvoika.count(c) != 0:
        return True
    else:
        return False


for num in range(0,10**9,2031):
    if num % 31 == 0:
        num_line = str(num)

        if num_line[:2] == "31" and num_line[-3] == "6" and num_line[-2] == "5": print(num, num/2031, F(num))
        if num_line[1:3] == "31" and num_line[-3] == "6" and num_line[-2] == "5": print(num, num/2031, F(num))
        if num_line[2:4] == "31" and num_line[-3] == "6" and num_line[-2] == "5": print(num, num/2031, F(num))
        if num_line[3:5] == "31" and num_line[-3] == "6" and num_line[-2] == "5": print(num, num/2031, F(num))
        if num_line[4:6] == "31" and num_line[-3] == "6" and num_line[-2] == "5": print(num, num/2031, F(num))'''



#60267
'''
for num in range (0,10**10,2024):
    num_line = str(num)
#1?2157*4
    if num_line[0] == "1" and num_line[2:6] == "2157" and num_line[-1] == "4":
        print(num,num/2024)'''

# Vasya
# РАЗОБРААААААААААААААТЬ
# c = 0
# for num in range(102, 10**12, 103):
#     print(num)
#     numString = str(num)
    # if numString[0] == '1' and numString[2:6] == '2139' and numString[-1] == '4':
    #     c += 1

# 27422
'''
def Delit(num):
    c = 0
    l = []
    for i in range(2, num//2 + 1):
        if num % i == 0:
            c += 1
            l.append(i)
        if c > 2:
            l.clear()
            return l
    if c == 2:
        return l
    else:
        l.clear()
        return l

for i in range(174457, 174506):
    if len(Delit(i)):
        print(Delit(i))'''





#27850
'''c = 0
for i in range(245690,245757):
    c+=1
    ok = True
    for j in range(2,i//2):
        if i%j == 0:
            ok = False
            break
    if ok == True:
        print(c, i)'''
#27851
'''c = 0
num = []
for i in range(210235,210301):
for i in range(210235,210301):
    c = 0
    for j in range(2,i//2+1):
        if i % j == 0:
            c+=1
            num.append(j)
        if c > 4:
            num.clear()
            break
    if c == 4:
        print(num)'''

#27856
'''def F(n):
    c = 0
    delitels = []
    for delit in range(1, n + 1, 2):
        if n % delit == 0:
            c += 1
            delitels.append(delit)
        if c > 6:
            return False
    if c == 6:
        return True, delitels
    else:
        return False

for n in range(95632, 95651):
    if F(n):
        t = F(n)[1]
        print(t)'''

#27858
'''c1 = 0
c2 = 0
for i in range(120115,120200+1):
    c = 1
    for n in range(1, i//2 +1):
        if i % n == 0:
            c+=1
            if c > c1:
                c1 = c
                c2 = i

print(c2,c1)'''

#28122
'''c2 = []
for i in range(489421, 489440+1):
    c = 0
    for n in range(1,i+1):
        if i % n  == 0:
            c+=1
            c2.append(n)
    if c == 4:
        print(c2)
        c2.clear()
    else:
        c2.clear()'''


#36880

for m in range(0, 31, 2):
    for n in range(1, 32, 2):
        num = 2**m * 3**n
        if 400_000_000 <= num and num <= 600_000_000:
            print(num)