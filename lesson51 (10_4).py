# Домашнее задание по теме "Очереди для обмена данными между потоками."
import random
import time
import threading
import queue
class Table():
    def __init__(self,number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        time.sleep(random.randint(3, 10))
        return


class Cafe():
    def __init__(self,*args):
        self.queue = queue.Queue() # args[-1]
        self.tables = args
    def __tables_is_free(self):
        for table_ in self.tables:
            if  not table_.guest is None: return False # есть занятый
        return True # нет занятых
    def _seating_to_table(self,table_, guest_):
        table_.guest = guest_  # сажаем
        table_.guest.start()
        print(f'{guest_.name} сел(-а) за стол номер {table_.number}')
        return
    def _seating_from_queue(self, table_):
        if table_.guest is None:  # проверяем свободен ли стол
            if not self.queue.empty():
                guest_ = self.queue.get()  # вызываем следующего из очереди
                print(f'{guest_.name} вышел из очереди')
                self._seating_to_table(table_,guest_)
        return
    def guest_arrival(self, *guests):

        guests = list(guests)
        guests.reverse()
        # рассаживаем кого можем по порядку (в очереди остаются те кому не хватило мест)
        for table_ in self.tables:
            if len(guests) >0:
                self._seating_to_table(table_, guests.pop())  # сажаем за стол
            else:
                print('Всех сразу рассадили')
        guests.reverse()
        # рассадили в пустой зал
        for guest_ in guests:
            print(f'{guest_.name} в очереди')
            self.queue.put(guest_)
        # а остальные остались в очереди, ждать
    def _guest_leaves(self, table_):
        print(f'{table_.guest.name} покушал(-а) и ушёл(ушла)')
        table_.guest.join()  # провожаем гостя
        print(f'Стол номер {table_.number} свободен')
        table_.guest = None  # освобождаем стол
        self._seating_from_queue(table_)  # сажаем за освобожденный стол
        return
    def discuss_guests(self):
        while not self.queue.empty() or not self.__tables_is_free():
            for table_ in self.tables:
                if not table_.guest is None:  # если стол занят
                    if table_.guest.is_alive():
                        continue # кушает ещё
                    else:
                         self._guest_leaves(table_)
        pass

# Проверка по заданию

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()