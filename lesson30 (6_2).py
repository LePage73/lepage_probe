# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."

class Vehicle:
    __COLOR_VARIANTS=['blue', 'red', 'green', 'black', 'white']
    def __init__(self,owner ,model, engine_power, color_):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color_
    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(self.get_model(),)
        print(self.__engine_power)
        print(self.get_color())
        print(self.owner)
    def set_color(self, new_color):
        if str(new_color).lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
            return
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5
    pass

#Исходный код:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

print(dir(Sedan))
print(dir(vehicle1))
print(dir(Vehicle))