from math import sqrt
class Figure:
    sides_count = 3
    name = ''
    def __init__(self,*args):
        self.__sides = []
        self.__color = []
        self.filled = False
        if isinstance(args[0], tuple):# проверяем правильно ли заполнены данные - первый элемент - кортеж RGB
            self.set_color(*args[0])# пытаемся установить цвет
        if isinstance(args[-1], bool): # проеряем последний элемент если bool то это заливка
            self.filled = args[-1]
            side_ = args[1:-1]
            self.set_sides(*side_)# оставшимся набором пытаемся заполнить стороны
        else:
            side_ = args[1:]
            self.set_sides(*side_)#
        self.__side_init_if_necessary()# проверяем заполнились ли стороны, если нет заполняем 1
        pass
    def __is_valid_color(self,*args):
        if len(args) != 3: return False
        if 0 > int(args[0]) or int(args[0]) > 255 or not isinstance(args[0],int): return False
        if 0 > int(args[1]) or int(args[1]) > 255 or not isinstance(args[1],int): return False
        if 0 > int(args[2]) or int(args[2]) > 255 or not isinstance(args[2],int): return False

        return True
    def set_color(self,*args):
        if self.__is_valid_color(*args):
            self.__color = []
            self.__color.insert(0,args[0])
            self.__color.insert(1,args[1])
            self.__color.insert(2,args[2])
        return
    def get_color(self):
        return self.__color
    def is_valid_sides(self,*args):
        if len(args) != self.sides_count: return False
        for side_ in args:
            if int(side_) < 0 or not isinstance(side_, int): return False
        return True
    def set_sides(self,*args):
        if self.is_valid_sides(*args):
            self.__sides = []
            for side_ in args:
                self.__sides.append(side_)
        return
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def __side_init_if_necessary(self):
        if not self.__sides:
            for i in range(0, self.sides_count):
                self.__sides.append(1)
        return
    def print_info(self):
        print('\nИмя фигуры: ',self.name)
        print('Цвет фигуры: ',self.get_color())
        print('Список сторон: ',self.__sides)
        print('Сумма длин сторон: ',self.__len__())
        if self.filled: print('Закрашена')
        else: print('Не закрашена')
        pass

class Circle(Figure):
    sides_count = 1
    __radius = 0
    def __init__(self,*args):
        super().__init__(*args)
        self.__radius = self.get_sides()[0] / 2 / 3.14
        self.name = 'Окружность'

    def get_square(self):
        return 3.14 * self.__radius**2
    def print_info(self):
        super().print_info()
        print('Площадь: ', self.get_square())

class Triangle(Figure):
    sides_count = 3
    __height = 0
    def __init__(self, *args):
        super().__init__(*args)
        self.__height = self.get_height()
        self.name = 'Треугольник'
        pass
    def get_height(self):
        a = self.get_sides()[0] # Используем формулу Герона - расcчитаем высоту по основанию а
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        s = self.__len__() /2
        return (2 * sqrt(s * (s - a) * (s - b) * (s - c))) / a

    def get_square(self):
        a = self.get_sides()[0] # Используем формулу Герона для площади
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        s = self.__len__() / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))

    def print_info(self):
        super().print_info()
        print('Площадь: ', self.get_square())
        print('Высота треугольника:', self.__height)

class Cube(Figure):
    sides_count = 12
    def __init__(self, *args):
        super().__init__(*args)
        self.name= 'Куб'
        pass
    def is_valid_sides(self,*args):
        if len(args) != 1: return False
        if int(args[0]) < 0 or not isinstance(args[0], int): return False
        return True
    def set_sides(self,*args):
        if self.is_valid_sides(*args):
            self.__sides = []
            for i in range(0, self.sides_count):
                self.__sides.append(args[0])

    def get_sides(self):
        return self.__sides
    def get_volume(self):
        print(self.get_sides())
        return self.get_sides()[0]**3
    def print_info(self):
        super().print_info()
        print('объем куба:', self.get_volume())




# мои проверки фигура
curve = Figure((22,22,22),1,2)
print(curve.get_sides())
print(curve.get_color())
curve.set_color(333,333,333)
print(curve.get_color())
curve.set_color(200,200,200)
print(curve.get_color())
curve.set_sides(3,2,1)
print(curve.get_sides())
curve.set_sides(3,2.5,1)
print(curve.get_sides())
curve.set_sides(3,2,1,4)
print(curve.get_sides())
print(curve.__len__())

# окружность
curve = Circle((100,200,300),6.28,True)
curve.print_info()
curve2 = Circle((100,200,210),7,True)
curve2.print_info()
curve3 = Circle((100,200,210),7,5,True)
curve3.print_info()
#треугольник
tre = Triangle((222,222,222),5,6,7,True)
tre.print_info()
tre2 = Triangle((111,111,111),1,2,3,4)
tre2.print_info()

cubik = Cube((12,12,12),5,True)
cubik.print_info()
print(cubik.get_sides())


cubik2 = Cube((15,15,15),5,7,False)
cubik2.print_info()

print('########################## проверка по заданию')

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
