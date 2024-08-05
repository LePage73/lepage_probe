# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции"

def personal_sum(numbers):
    summ = 0
    incorrect_data = 0
    for i in numbers:
        try:
            summ += i
        except TypeError:
            print(f'Некорректное значение "{i}" для посчета суммы')
            incorrect_data +=1
    return (summ, incorrect_data)

def calculate_average(numbers):
    try:
        return personal_sum(numbers)[0]/ len(numbers)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В "{numbers}" записан некорректный тип данных')
        return None

# Проверка по заданию
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать