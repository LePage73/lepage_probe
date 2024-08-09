# Домашнее задание по теме "Многопроцессное программирование"
from secundomer import Timer
import multiprocessing

timer_ = Timer('first')
list_files = [f'.\\Files\\File {x}.txt' for x in range(1, 5)]

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            string_ = file.readline()
            if len(string_) == 0: return
            all_data.append(string_)

# Проверка по заданию
if __name__ == '__main__':
    timer_.start()
    for file_ in list_files:
        read_info(file_)
    timer_.stop()
    print('Время линейного исполнения: ', timer_)
# 0:00:06.200409

if __name__ == '__main__':
    timer_.start()
    with multiprocessing.Pool(processes=12) as pool:
        pool.map(read_info, list_files)
    timer_.stop()
    print('Время многопроцессорного исполнения: ', timer_)
# 0:00:02.696786

