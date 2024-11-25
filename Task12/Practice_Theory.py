# 9365
'''x = '8' * 68
while (('222' in x) or ('888' in x)):
    if '222' in x:
        x = x.replace('222', '8', 1)
    else:
        x = x.replace('888', '2', 1)

print(x)'''

#9764
'''x = '9' * 127

while (('333' in x) or ('999' in x)):
    if '333' in x:
        x = x.replace('333', '9', 1)
    else: x = x.replace('999', '3', 1)

print(x)'''

#18820

'''x = '9' * 65

while (('999' in x) or ("222" in x)):
    if ('222' in x): x = x.replace("22", "9", 1)
    else: x = x .replace("999", "2", 1)
print(x.count('9') * 9 + x.count('2') * 2)'''

#23912

'''x = ">" + "1" * 10 + "2" * 20 + "3" * 30

while ((">1" in x) or ('>2' in x) or ('>3' in x)):
    if ('>1' in x): x = x.replace('>1',"22>",1)

    if ('>2' in x): x = x.replace('>2', '2>', 1)

    if ('>3' in x): x = x.replace('>3', '1>', 1)

print(x.count('2') * 2 + x.count('1'))'''

#27272

'''for j in range(61,150):
    x = '1' * j
    while ('111' in x):
        x = x.replace('111','2',1)
        x = x.replace('222','11',1)
    if x == '2211':
        print(j)
        break'''

#35470

'''for odin in range(1,100):
    for duo in range(1,100):
        for tres in range(1,100):
            x = '0' + '1' * odin + '2' * duo + '3' * tres
            while (('01' in x) or ('02' in x) or ('03' in x)):
                x = x.replace('01', '2302', 1)
                x = x.replace('02', '10', 1)
                x = x.replace('03', '201', 1)
            if ((x.count('1') == 40) and (x.count('2') == 10) and (x.count('3') == 8)):
                print(odin)'''

#38946


'''for i in range(201,500):
    x = '1' * i
    while(('111' in x) or ('222' in x)):
        x = x.replace('111','22',1)
        x = x.replace('222','1',1)
    if x.count('2') == 0:
        print(i)'''

#45246

'''x = '8' * 84

while(('1111' in x) or('8888' in x)):
    if "1111" in x:
        x = x.replace('1111','8',1)
    else: x = x.replace('8888','11',1)
print(x)'''

from datetime import datetime
#48433
now = datetime.now()
for i in range(1,100):
    x = '0' +'1' * i + '2' * i + '0'
#    print(x)
    while (not('00' in x)):
        x = x.replace('011','20',1)
 #       print(x)
        x = x.replace('022','10',1)
  #      print(x)
        x = x.replace('01','220',1)
   #     print(x)
        x = x.replace('02','110',1)
    #    print(x)
     #   print(x.count('2'), (x.count('1')))

        if (x.count('1') == 40) and (x.count('2') > 50):
            print(x.count('2'))
            break

# i = 0
# c = 0
# while c == 0:
#     x = '0' + '1' * i + '2' * i + '0'
#     while '00' not in x:
#         x = x.replace('011', '20', 1)
#         x = x.replace('022', '10', 1)
#         x = x.replace('01', '220', 1)
#         x = x.replace('02', '110', 1)
#
#         if (x.count('1') == 40) and (x.count('2') > 50) and c == 0:
#             c = 1
#     i += 1
now1 = datetime.now()
print(now1 - now)

