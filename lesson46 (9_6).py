# Домашнее задание по теме "Генераторы"

def all_variants(text):
    i, j = 0, 0
    while i < len(text) and j <= len(text):
        j += 1
        yield text[i: j]
        if j == len(text):
            i += 1
            j = i


a = all_variants("abc")
for i in a:
    print(i)

