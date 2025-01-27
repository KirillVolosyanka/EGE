#45259
'''
for num in range(0, 10**9, 23):
    num_line = str(num)
    if num_line[0] == "1" and num_line[1] == "2" and num_line[2] == "3" and num_line[3] == "4" and num_line[4] == "5" and num_line[-3] == "7" and num_line[-1] == "8":
        print(num, num / 23)'''

#47229

'''for num in range(0, 10**10, 2023):
    num_line = str(num)
    if num_line[0] == "1" and num_line[2] == "2" and num_line[3] == "1" and num_line[4] == "3" and num_line[5] == "9" and num_line[-1] == "4":
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

def F(num):
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

        if num_line[:2] == "31" and num_line[-3] == "6" and num_line[-2] == "5": print(num, num/2031)
        if num_line[1:3] == "31" and num_line[-3] == "6" and num_line[-2] == "5": print(num, num/2031)
        if num_line[2:4] == "31" and num_line[-3] == "6" and num_line[-2] == "5": print(num, num/2031)
        if num_line[3:5] == "31" and num_line[-3] == "6" and num_line[-2] == "5": print(num, num/2031)
        if num_line[4:6] == "31" and num_line[-3] == "6" and num_line[-2] == "5": print(num, num/2031)

print(F(53831655))

#53831655
