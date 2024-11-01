'''
The main rule is
"A -> B = not(A) or B"
'''

# 9804
'''
for a in range (1, 65):
    Ok=1
    for x in range (0, 65):
        if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))) == 0:
            Ok=0
    if Ok:
        print(a)
        break
'''

