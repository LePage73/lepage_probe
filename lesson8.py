# Словари и множества

my_dict = {'Name': 'Igor',
           'Age': 54}
print('Словарь:',my_dict)
print('Существующая пара:',my_dict['Name'])
print('Несуществующая пара с ключом Birthday:', my_dict.get('Birthday'))
my_dict.update({'Birthday': '27.07',
                'City': 'Ulyanovsk'})
print('Словарь после добавления:',my_dict)
print('Извлекаем значение ключа Age:', my_dict.pop('Age'))
print('Словарь после извлечения ключа Age:',my_dict)

my_set = {'мама','мыла','раму','раму','мыла','мама'}
print('Множество:', my_set)
my_set.update({'встав','на подоконник', 3})
print('Множество после добавления 3-х элементов:', my_set)
my_set.discard('на подоконник')
my_set.discard(3)
print('Множество после удаления элениента "на подоконник" и числа 3:', my_set)
