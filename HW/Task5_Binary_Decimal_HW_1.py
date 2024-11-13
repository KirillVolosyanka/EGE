# Number 1

# nuhuya ne ponyal vobshe

'''MaxLenRs = []
for n in range(1,500):
    R = bin(n) [2::]
    decDiv = n % 4
    binDiv = bin(decDiv)[2::]
    R += str(binDiv)
    R = int(R,2)
    R = bin(R)[2::]
    print(R)
    res = int(R,2)
    MaxLenRs.append(res)


print(max(MaxLenRs))'''


# Answer:

'''_________________________________________________________________________'''

# Number 2
'''
'''
# da v pizdu, ya nihuya ne znau
# Answer:

'''_________________________________________________________________________'''

# Number 3

''''''

# Answer:

'''_________________________________________________________________________'''

# Number 4
''' '''
# Answer:

'''_________________________________________________________________________'''

# Number 5
''' '''


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
