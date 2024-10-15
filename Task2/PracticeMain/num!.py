'''
A -> B = not(A) or B. OUT OF USE: <=!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 ≡ - ==
 ∨ - or
 ∧ - and
 ¬ - not
'''

# 15939
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (z and y) or ((not(x) or z) == (not(y) or w))
                if f == 0:
                    print(x, y, z, w)





