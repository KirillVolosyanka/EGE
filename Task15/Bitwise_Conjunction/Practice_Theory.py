'''
The main rule is
"A -> B = not(A) or B"
'''

# 9804
'''
for a in range (1, 65):
    Ok=True
    for x in range (0, 65):
        if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))) == 0:
            Ok=False
    if Ok:
        print(a)
        break
'''

#Яндекс ЕГЭ
# https://education.yandex.ru/ege/task/4cb47800-ed22-4851-98b4-dcee23fc0448

# for a in range (1,899):
#     Ok = 1
#
#     for x in range (10,100):
#         if (not((x | 41 == 0) or (x & 128 != 0))
#                 and (x & a == 0)
#                 and ((x | a == 0) or (x & a == 0))):
#             Ok=0
#
#     if Ok:
#         print(a)
#         break

#Яндекс ЕГЭ
#https://education.yandex.ru/ege/task/9785715a-76a3-4747-8ae6-fe6a56597181
#
# count = 0
# for a in range (1, 999):
#     ok = True
#
#     for x in range (0,1000):
#         if ((x & 13 == 0) and (x & 18 != 0) or ((x & 21!=0) or ((x & a==0)
#                                                           and (x & 21==0)))) == 1:
#             ok = False
#
#     if ok:
#         count+=1
#         print(count)
#         break
#
# print(count)

