#Условная конструкция. Операторы if, elif, else.

# решение без логических операторов

first = input('Первое число ')
second = input('Второе число ')
third = input('Третье число ')

if first == second == third :
    print('Результат: ',3)
elif first != second != third :
    print('Результат: ',0)
else :
    print('Результат: ',2)

# решение с логическими операторами

if first == second and second == third :
    print('Результат с логическими операторами: ', 3)
elif first != second and second != third and first != third :
    print('Результат с логическими операторами: ', 0)
else :
    print('Результат с логическими операторами: ',2)
