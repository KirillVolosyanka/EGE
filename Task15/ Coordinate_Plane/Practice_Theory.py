"""
    Main formula is A -> B = not(A) or B
"""

# 15
for a in range(0, 500):
    Ok = True
    for x in range(0, 500):
        for y in range(0, 500):
            if (not(x <= 9) or (x * x <= a)) and (not(y*y <= a) or (y <= 9)) == False:
                Ok = False
                break
    if Ok:
        print(a)

#14704
# count = 0
# for a in range (0,500):
#     ok = True
#     for x in range(0,500):
#         for y in range (0,500):
#             if ((not(x < 6) or (x**2 < a)) and (not(y**2 <= a) or (y <= 6))) == False:
#                 ok = False
#                 break
#     if ok:
#         count += 1
#
# print(count)

#16393
#
# for a in range (0,500):
#     ok = True
#     for x in range (0,500):
#         for y in range (0,500):
#             if (((2*x + 3*y) > 30) or ((x + y) <= a)) == False:
#                 ok = False
#                 break
#
#     if ok:
#         print(a)

#15803 (отрезок)
#
# def func(x, up, down):
#     return ((not(down <= x and x <= up)) or (x**2 <= 100)) and (not(x**2 <= 64) or (down <= x and x <= up))
#
# for down in range (-500,500):
#     # print("Down = ", down)
#     for up in range(down + 1, 500 + 1):
#         ok = True
#         for x in range (-1000, 1000):
#             f = func(x,up, down)
#             if f == False:
#                 ok = False
#                 break
#         if ok:
#             print(up - down)