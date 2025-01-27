#45259
'''
for num in range(0, 10**9, 23):
    num_line = str(num)
    if num_line[0] == "1" and num_line[1] == "2" and num_line[2] == "3" and num_line[3] == "4" and num_line[4] == "5" and num_line[-3] == "7" and num_line[-1] == "8":
        print(num, num / 23)'''

#47229

for num in range(0, 10**10, 2023):
    num_line = str(num)
    if num_line[0] == "1" and num_line[2] == "2" and num_line[3] == "1" and num_line[4] == "3" and num_line[5] == "9" and num_line[-1] == "4":
        print(num, num / 2023)