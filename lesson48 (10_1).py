# Домашнее задание по теме "Создание потоков".
import time
from threading import Thread
from datetime import datetime
from time import sleep



def write_words(*args):
    word_count = args[0]
    file_name = args[1]
    with open(file_name, 'w', encoding='utf-8') as file_ :
        for i in range(1, word_count):
            file_.write(f'Какое-то слово № {i}\n' )
    time.sleep(0.5)
    print(f'Завершилась запись в {file_name}')

#
start_time_ = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
print(f'Время работы функций  {datetime.now() - start_time_}')

thr1 = Thread(write_words(10, 'example5.txt'))
thr2 = Thread(write_words(30, 'example6.txt'))
thr3 = Thread(write_words(200, 'example7.txt'))
thr4 = Thread(write_words(100, 'example8.txt'))

start_time_ = datetime.now()
thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()
print(f'Время работы в потоках {datetime.now() - start_time_}')
