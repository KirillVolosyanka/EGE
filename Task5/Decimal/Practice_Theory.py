# 7763
for i in range(100, 1000):
    start_num = str(i)
    num1 = int(start_num[0]) + int(start_num[1])
    num2 = int(start_num[1]) + int(start_num[2])
    first = str(max(num1, num2))
    second = str((min(num1, num2)))
    end_num = first + second
    if end_num == '1412':
        print(i)
        break