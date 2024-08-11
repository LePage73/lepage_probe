# Домашнее задание по теме "Позиционирование в файле"

def custom_write(file_name, *strings):
    file = open(file_name, "w", encoding='utf-8')
    str_num = 0
    dict_ = {}
    for str_ in strings[0]:
        str_num += 1
        dict_.update({(str_num, file.tell()): str_})
        file.write(str(str_ + '\n'))


    file.close()
    return dict_

info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
