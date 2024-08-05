# Домашнее задание по теме "Try и Except"

def add_everything_up(a, b):
    try:
        return a + b
    except: # одна из переменных не число
        return str(a) + str(b) # переводим оба аргумента в строки и складываем строки


# проверка по заданию
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
