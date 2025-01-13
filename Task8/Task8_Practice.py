# 8098
'''
letters = "СЛОН"
c = 0
for n1 in letters:
    for n2 in letters:
        for n3 in letters:
            for n4 in letters:
                for n5 in letters:
                    word = n1 + n2 + n3 + n4 + n5
                    if word.count('С') == 1:
                        c += 1
print(c)
'''
#16385
'''
letters = 'АБВГД'
letterss = 'БВГД'
c = 0
for n1 in letterss:
    for n2 in letters:
        for n3 in letters:
            for n4 in letters:
                for n5 in letters:
                    word = n1 + n2 + n3 + n4 + n5
                    if not(("ББ" in word) or ("ВВ" in word) or ("ГГ" in word) or ("ДД" in word) or ("АА" in word)):
                        c+=1
print(c)'''
#16813

'''letter = "ЛЕВИЙ"
c = 0
for n1 in letter:
    for n2 in letter:
        for n3 in letter:
            for n4 in letter:
                for n5 in letter:
                    word = n1 + n2+ n3 + n4 + n5
                    if not("ЕИ" in word):
                        if ((word.count("Й") == 1) and (word.count("Л") == 1) and (word.count("Е") == 1) and (word.count("И") == 1) and (word.count("В") == 1)):
                            if n1 != "Й":
                                c+=1
print(c)'''

#58516

'''alpha = "ВИКОРТ"
c=0
for n1 in alpha:
    for n2 in alpha:
        for n3 in alpha:
            for n4 in alpha:
                for n5 in alpha:
                    for n6 in alpha:
                        word = n1+n2+n3+n4+n5+n6
                        if word.count("В") == 1 and word.count("И") == 1 and word.count("К") == 1 and word.count("Т") == 1 and word.count("О") == 1 and word.count("Р") == 1:
                            c+=1
                            print(word, c)
                        if c  ==170:
                            print(word)'''

from functools import cache
@cache
def f(n):
    n = str(n)
    num = []

    if len(n) == 11:
        return 1

    for i in range(0,9):
        if ((int(n[-1]) + i) % 2 == 0) and  int(n[-1]) < i:
            num.append(int(n + str(i)))
        elif ((int(n[-1]) + i) % 2 != 0) and  int(n[-1]) > i:
            num.append(int(n + str(i)))

    return sum(f(i) for i in num)

print(sum(f(i)for i in range(1,9)))
