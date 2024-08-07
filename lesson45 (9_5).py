# Домашнее задание по теме "Итераторы"

class StepValueError(ValueError):
    pass

class Iterator():
    def __init__(self, *args):
        self.start = args[0]
        self.stop = args[1]
        try:
            self.step = args[2]
        except IndexError: # недостаточно аргументов
            if self.start <= self.stop: self.step = 1 # задаем шаг по умолчанию от меньшего к большему
            else: self.step = -1 # задаем шаг по умолчанию от большего к меньшему
        self.pointer = self.start
        if self.step == 0: raise StepValueError()
    pass

    def __iter__(self):
        self.pointer = self.start - self.step # Начнем сначала :)
        return self

    def __next__(self):
        self.pointer += self.step
        if self.step < 0 and self.pointer < self.stop: raise StopIteration()
        if self.step > 0 and self.pointer > self.stop: raise StopIteration()
        return self.pointer

# Проверка по заданию
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1: print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()