# Самостоятельная работа по уроку "Распаковка позиционных параметров"

def print_params(a = 1, b = 'строка', c = True):
    print(a, b ,c)

print('1.Функция с параметрами по умолчанию:')
print_params()
print_params(b = 25) # работает вместо строки - 25
print_params(c=[1, 2, 3]) # работает вместо true - [1,2,3]

print('2.Распаковка параметров:')
values_list = ['String', False, 55]
values_dict = {'a':'String', 'b': False, 'c': 55}
print('Список', values_list)
print('Словарь', values_dict)
print_params(*values_list)
print_params(**values_dict)

print('3.Распаковка + отдельные параметры:')
values_list_2 = [54.32, 'Строка' ]
print('Список', values_list_2)
print_params(*values_list_2, 42)
