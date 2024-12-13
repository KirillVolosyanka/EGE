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

letter = "ЛЕВИЙ"
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
print(c)