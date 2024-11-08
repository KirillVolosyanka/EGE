# 7763
'''for i in range(100, 1000):
    start_num = str(i)
    num1 = int(start_num[0]) + int(start_num[1])
    num2 = int(start_num[1]) + int(start_num[2])
    first = str(max(num1, num2))
    second = str((min(num1, num2)))
    end_num = first + second
    if end_num == '1412':
        print(i)
        break'''

#8654

'''for i in range (1000, 10_000):
    startNum = str(i)
    num1 = int(startNum[0]) * int(startNum[1])
    num2 = int(startNum[2]) * int(startNum[3])
    firstNum = str(max(num1,num2))
    secondNum = str(min(num1,num2))
    endNum = firstNum + secondNum
    if endNum == "124":
        print(i)
        break
'''


#68238

for i in range(1000,2000):
    startNum = str(i)
    num1 = startNum[0] + startNum[1] + startNum[2]
    num2 = startNum[1] + startNum[2] + startNum[3]
    endNum = abs(int(num1) - int(num2))
    if endNum == 415:
        print(i)
        break


