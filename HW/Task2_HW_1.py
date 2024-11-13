# Number 1

'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = ((not(x) or y) or (not(z) or w)) and (not(z == y) or (w == x))
                f =
                # f = (y or (not(x))) or (w or (not (z))) and ((w == x) or (not (z == y)))
                if f == 0:
                    print(x, y, z, w)
'''
# Answer: done

'''_________________________________________________________________________'''

# Number 2
'''
print("x y z")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            f = (not(x or y) or (z == x))
            if f == 0:
                print (x,y,z)
'''
# Answer: xzy Right

'''_________________________________________________________________________'''

# Number 3

'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                # Right version ((not(w) or not(x)) == (not(z) or y)) and (y or w)
                f = (not(w) or not(x) == (not(z) or y)) and (y or w)
                if f == 1 and y == 0:
                    print(x, y, z, w)
'''

# Answer: wxyz NOT Right

'''_________________________________________________________________________'''

# Number 4
'''
print("x y z w")

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:

                f1 = (not(w or not(y)) or (z == x))
                f2 = (w or not(y)) == (not(x) or z)
                if (f1 == 0) and (f2 == 0):

                    print(x, y, z, w)
'''
# Answer: done

'''_________________________________________________________________________'''

# Number 5
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
            for z in 0,1:
                for w in 0,1:
                    f = ((not(x == z) or (not(y) or w)) == (not((not(w) or z) or (not(x) or y))))
                    if f == 1:
                        print(x, y, z, w)
'''


# Answer: zyxw Right

'''_________________________________________________________________________'''

# Number 6
'''
    Code is here
    I let you don't make this, because we did it)))
'''
# Answer: _ _ _ _

'''_________________________________________________________________________'''

# Number 7
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
            for z in 0,1:
                for w in 0,1:
                    f = ((not(not(z == w)) or (w and(not(x)))) or (x and not(y)))
                    if f == 0 and w == 0:
                        print(x, y, z, w)
'''

# Answer: wzyx Right

'''_________________________________________________________________________'''

# Number 8

'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = ((x and y and (not(z))) == (y or z or(not(w))))
                if f == 1:
                    print(x,y,z,w)
'''
# Answer: wyzx Right

'''_________________________________________________________________________'''

# Number 9
'''
print("x y z")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:

            f = ((x == y) or (not(y or z) or x))
            if f == 0:
                print(x,y,z)
'''
# Answer: xzy Right

'''_________________________________________________________________________'''

# Number 10

'''print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not(y or z) or (z and w)) == (not(not(x and z) or (w or y)))
                if f == 1 and y == 1 and z == 1:
                    print(x,y,z,w)
'''
# Answer: wyxz Right

'''_________________________________________________________________________'''

# Number 11

'''print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not(x and y) or (not(z) or w)) and ((not(w) or x) or not(y))
                if f == 0:
                    print(x,y,z,w)
'''
# Answer: zwyx Right

'''_________________________________________________________________________'''

# Number 12

'''print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = ((not(w) or x) or (not(y) or z)) and (not(x == y) or (w == z))
                if f == 0 and z == 0 and w ==1:
                    print(x,y,z,w)
'''
# Answer: xzwy Right

'''_________________________________________________________________________'''

# Number 13

'''print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not((x and not(y)) == (z or not(w))) or (x and z))
                if f == 0 and w ==1:
                    print(x,y,z,w)
'''
# Answer: yzwx Right

'''_________________________________________________________________________'''

# Number 14

'''print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f1 = (not(x) or y) == (w or not(z))
                f2 = (not(x) or y) and (not(w) == z)
                if f1 == 1 and f2==0 and z ==1:
                    print(x,y,z,w)
'''
# Answer: xzyw Right

'''_________________________________________________________________________'''

# Number 15

print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not((x or not(y)) and (not(z) == w)) or (y and z)
                if f == 0:
                    print(x,y,z,w)

# Answer: xzwy/yxzw everyone isn't right
