a = 3
b = 4
c = 5

if max(a,b,c) < min(a,b,c) + (a+b+c-max(a,b,c)- min(a,b,c)):
    print("any треугольник exists")

if max(a,b,c)**2 == min(a,b,c)**2 + (a+b+c-max(a,b,c)- min(a,b,c))**2:
    print("прямоугольный треугольник exists")

if max(a,b,c)**2 > min(a,b,c)**2 + (a+b+c-max(a,b,c)- min(a,b,c))**2:
    print("тупоуг треугольник exists")

if max(a,b,c)**2 < min(a,b,c)**2 + (a+b+c-max(a,b,c)- min(a,b,c))**2:
    print("остроуг треугольник exists")





