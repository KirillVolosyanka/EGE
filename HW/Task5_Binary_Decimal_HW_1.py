'''1, 3 and 5 do'''

# Number 1

# nuhuya ne ponyal vobshe
'''
MaxLenRs = [0] * 10000
for n in range(1,1000):
    R = bin(n) [2:]
    decDiv = n % 4
    binDiv = bin(decDiv)[2:]
    R += str(binDiv)
    R = int(R,2)
    MaxLenRs[R] = 1
print(MaxLenRs)



maxSumLenRes = 0
for i in range(10_001 - 49):
    maxSumLenRes = max(maxSumLenRes, sum(MaxLenRs[i : i + 49]))


print(maxSumLenRes)
'''

# Answer: 19
'''_________________________________________________________________________'''

# Number 2
'''for n in range(1,5000):

    binN = str(bin(n)[2::])
    chN = 0
    chN += binN.count("1")
    binN = binN + str(chN % 2)

    chN = 0
    chN += binN.count("1")
    binN = binN + str(chN % 2)

    if (int(binN, 2) > 97):
        print(int(binN, 2))
        break'''
# Answer: 102

'''_________________________________________________________________________'''

# Number 3
'''
for n in range(0,255):

    binN = str(bin(n)[2::])
    binN8 = format(n, '08b')
    #print(binN)
    #print(binN8)
    binN8 = binN8.replace('0', 'X').replace('1', '0').replace('X', '1')
    #print(binN8)
    intN = int(binN8, 2)
    res = n - intN

    if res == 111:
        #print(n)
        print(intN)'''
# ya hz pochemu no ono rabotaet
# Answer:

'''_________________________________________________________________________'''

# Number 4
# 1. СТРОИТСЯ ДВОИЧНАЯ ЗАПИСЬ ЧИСЛА N.
# 2. ДАЛЕЕ ЭТА ЗАПИСЬ ОБРАБАТЫВАЕТСЯ ПО СЛЕДУЮЩЕМУ ПРАВИЛУ:
# А) ЕСЛИ ЧИСЛО ЧЁТНОЕ, ТО К ДВОИЧНОЙ ЗАПИСИ ЧИСЛА СЛЕВА ДОПИСЫВАЕТСЯ 10;
# Б) ЕСЛИ ЧИСЛО НЕЧЁТНОЕ, ТО К ДВОИЧНОЙ ЗАПИСИ ЧИСЛА СЛЕВА ДОПИСЫВАЕТСЯ 1 И СПРАВА ДОПИСЫВАЕТСЯ 01.
# ПОЛУЧЕННАЯ ТАКИМ ОБРАЗОМ ЗАПИСЬ ЯВЛЯЕТСЯ ДВОИЧНОЙ ЗАПИСЬЮ ИСКОМОГО ЧИСЛА R.
# 3. РЕЗУЛЬТАТ ПЕРЕВОДИТСЯ В ДЕСЯТИЧНУЮ СИСТЕМУ И ВЫВОДИТСЯ НА ЭКРАН.

'''for n in range(0,12):
    binN = str(bin(n)[2::])
    if n % 2 ==0:
        binN = "10" + binN
    else:
        binN = "1" + binN +"01"

    r = int(binN,2)
    if n <=12:
        print(r)'''
# Answer: 109

'''_________________________________________________________________________'''

# Number 5
#1. СТРОИТСЯ ДВОИЧНАЯ ЗАПИСЬ ЧИСЛА N.
#2. ВЫЧИСЛЯЕТСЯ КОЛИЧЕСТВО ЕДИНИЦ, СТОЯЩИХ НА ЧЁТНЫХ МЕСТАХ В ДВОИЧНОЙ ЗАПИСИ ЧИСЛА N БЕЗ ВЕДУЩИХ НУЛЕЙ, И КОЛИЧЕСТВО НУЛЕЙ,
# СТОЯЩИХ НА НЕЧЁТНЫХ МЕСТАХ. МЕСТА ОТСЧИТЫВАЮТСЯ СЛЕВА НАПРАВО (ОТ СТАРШИХ РАЗРЯДОВ К МЛАДШИМ, НАЧИНАЯ С ЕДИНИЦЫ).
#3. РЕЗУЛЬТАТОМ РАБОТЫ АЛГОРИТМА СТАНОВИТСЯ МОДУЛЬ РАЗНОСТИ ПОЛУЧЕННЫХ ДВУХ ЧИСЕЛ.

def sumChNech(binN):
    c0 = 0
    c1 = 0
    for i in range(0, len(binN), 2): #Nech
        if binN[i] == "0":
            c0 += 1
    for i in range(1, len(binN), 2): #Nech
        if binN[i] == "1":
            c1 += 1
    return abs(c1-c0)


for n in range(1,1024):
    binN = bin(n)[2::]
    binN = str(binN)
    if sumChNech(binN) == 5:
        print(int(binN, 2))



# Answer:

'''_________________________________________________________________________'''

# Number 6
''' for i in range(1000,10_000):
    res = []
    startNumM = str(i)
    num1 = int(startNumM[0]) + int(startNumM[1])
    num2 = int(startNumM[1]) + int(startNumM[2])
    num3 = int(startNumM[2]) + int(startNumM[3])
    res.append(num1)
    res.append(num2)
    res.append(num3)
    res.sort()
    endNum = str(res[1]) + str (res[2])

    if endNum == "1418":
        print(i)
'''
# Answer: 1599
'''_________________________________________________________________________'''
# Number 7
''' 
for i in range(100,1000):
    startNumM = str(i)
    num1 = int(startNumM[0]) + int(startNumM[1])
    num2 = int(startNumM[1]) + int(startNumM[2])
    first = str(max(num1,num2))
    sec = str(min(num1,num2))
    endNum = first + sec

    if endNum == "159":
        print(i)
        break'''


# Answer: 187

'''_________________________________________________________________________'''

# Number 8

''' for i in range(100,1000):
    startNum = str(i)
    num1 = int(startNum[0]) + int(startNum[1])
    num2 = int(startNum[1]) + int(startNum[2])
    first = str(min(num1,num2))
    second = str(max(num1, num2))
    endNum = first + second

    if endNum == "812":
        print(i)
        break  '''


# Answer: 175

'''_________________________________________________________________________'''

# Number 9
''' for i in range(100,1000):
    startNum = str(i)
    num1 = int(startNum[0]) * int(startNum[1])
    num2 = int(startNum[1]) * int(startNum[2])
    fst = str(max(num1,num2))
    sec = str(min(num1,num2))
    endNum = fst + sec

    if endNum == "123":
        print(i)
        break '''

# Answer: 134

'''_________________________________________________________________________'''

# Number 10
'''for i in range(100,1000):
    startNum = str(i)
    num1 = int(startNum[0]) + int(startNum[1])
    num2 = int(startNum[1]) + int(startNum[2])
    maxi = str(max(num1,num2))
    mini = str(min(num1,num2))
    endNum = mini + maxi

    if endNum == "1115":
        print(i)
        break'''
# Answer: 296

'''_________________________________________________________________________'''
