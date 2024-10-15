"""
    Main formula is A -> B = not(A) or B
"""

# 13745
for a in range(1, 300):
    Ok = True
    for x in range(0, 500):
        for y in range(0, 500):
            if (not(x <= 9) or (x * x <= a)) and (not(y*y <= a) or (y <= 9)) == False:
                Ok = False
                break
    if Ok:
        print(a)