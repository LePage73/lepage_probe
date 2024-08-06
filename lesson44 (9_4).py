# Домашнее задание по теме "Создание функций на лету"
import random
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x,y: x==y, first, second)))

# функция
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, "w", encoding="utf-8") as file:
            for data_ in data_set:
                file.write(str(data_)+'\n')

    return write_everything

write = get_advanced_writer('example.txt') # была переменной
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке']) # стала функцией

# класс
class MysticBall:
    def __init__(self,*words):
        self.words = words
        pass
    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())