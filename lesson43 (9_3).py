# Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x[0]) - len(x[1]) for x in zip(first,second) if len(x[0]) - len(x[1]) != 0)
second_result = (True if len(first[x]) == len(second[y]) else False for x in range(0, len(first)) for y in range(0, len(second)) if x==y)

# проверка по заданию
print(list(first_result))
print(list(second_result))