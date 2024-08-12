# Домашнее задание по теме "Интроспекция"

from pprint import pprint
import secundomer

def introspection_info(obj):
    dict_ = {}
    # Определяем тип
    dict_.update({'1_Тип': type(obj)})
    # Находим все аттрибуты
    dict_.update({'2_Атрибуты': dir(obj)})
    # находим все методы
    list_method = [attr for attr in dir(obj) if callable(getattr(obj, attr)) and attr.startswith('__') is False]
    dict_.update({'3_Методы': list_method})
    # определяем модуль
    if hasattr(obj, '__module__'):
        dict_.update({'4_Модуль': obj.__module__})
    else:
        dict_.update({'4_Модуль': "__main__"})
    # Определяем Док-ю
    if hasattr(obj, '__doc__'):
        dict_.update({'5_Док': obj.__doc__})

    return dict_



# Объекты для проверки
#####################################################################
a = 42
b = {}
c = []
d = ()

timer_ = secundomer.Timer('test')

def some_func():
    pass
class some_class:
    def some_method(self):
        # return
        pass
#####################################################################
obj = timer_
number_info = introspection_info(obj)
pprint(number_info)

