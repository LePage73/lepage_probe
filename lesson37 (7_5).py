# Домашнее задание по теме "Файлы в операционной системе"

import os
import time

directory = "test"

for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_time = os.path.getmtime(file_path)
            file_time_formatted =  time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
            file_size = os.path.getsize(file_path)
            file_parent_dir = os.path.dirname(file_path)
            print(f'Файл: {file}, '
                  f'Путь: {file_path}, '
                  f'Размер: {file_size}, '
                  f'Время изменения: {file_time_formatted}, '
                  f'Родительский каталог: {file_parent_dir} ')

