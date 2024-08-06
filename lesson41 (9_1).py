# Домашнее задание по теме "Введение в функциональное программирование

def apply_all_func(*args):
    dict_ = {}
    for func_ in list(args[1:]):
        dict_.update({func_.__name__: func_(args[0])})
    return dict_

# проверка по заданию
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
