# Дополнительное практическое задание по модулю: "Наследование классов."
from math import sqrt
class Figure:
    sides_count = 0
    name = ''
    def __init__(self, *args):
        self.__color = [255, 255, 255]
        self.__sides = []
        self.filled = False
        args = list(args)
        if isinstance(args[-1],bool):
            self.filled = args.pop()
        args.reverse()
        color_ = list(args.pop())
        if self.__is_valid_color(color_[0],color_[1],color_[2]):
            self.set_color(color_[0],color_[1],color_[2])
        if self.__is_valid_sides(*args):
            self.set_sides(*args)
        else:
            for i in range(0,self.sides_count):
                self.__sides.append(1)


    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 > r or r > 255:
            return False
        if 0 > g or g > 255:
            return False
        if 0 > b or b > 255:
            return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        sides = list(sides)
        if len(sides) == self.sides_count:
            valid_side_ = True
            for side in sides:
                if side < 0 or not isinstance(side,int):
                    valid_side_ = False
            return valid_side_
        return False
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        return

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimetr_ = 0
        for side in self.__sides:
            perimetr_ += side
        return perimetr_


    def print_info(self):
        print('\nНазвание: ', self.name)
        print('Цвет: ', self.get_color())
        print('Длины сторон:',self.get_sides())
        print('Сумма длин сторон:', self.__len__())
        if self.filled:
            print('Есть заливка')
        else:
            print('Прозрачная фигура')

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
        print(self.get_sides())
        a = self.get_sides()[0] # Используем формулу Герона - расчитаем высоту по основанию а
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

    def __init__(self,*args):
        self.__sides = []
        super().__init__(*args)
        args = list(args)
        args.pop()
        args.reverse()
        args.pop()
        if len(args) == 1 and isinstance(args[0],int):
            for i in range(0, self.sides_count):
                self.__sides.append(args[0])
        else:
            for i in range(0, self.sides_count):
                self.__sides.append(1)

        self.name = 'Куб'
        pass
    def __is_valid_sides(self, sides):
        if len(sides) == 1:
            valid_side_ = True
            if sides[0] < 0 or not isinstance(sides[0],int):
                valid_side_ = False
            return valid_side_
        return False
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(list(new_sides)):
            self.__sides = new_sides
        return
    def get_sides(self):
        return self.__sides
    def get_volume(self):
        return self.get_sides()[0]**3
    def print_info(self):
        super().print_info()
        print('объем куба:', self.get_volume())





# мои проверки
print(dir(Circle))
curve = Circle((100,200,300),6.28,True)
curve.print_info()
curve2 = Circle((100,200,210),7,True)
curve2.print_info()
curve3 = Circle((100,200,210),7,5,True)
curve3.print_info()

tre = Triangle((222,222,222),5,6,7,True)
print(tre.get_sides())
tre.print_info()
tre2 = Triangle((111,111,111),1,2,3)
print(tre2.get_sides())
tre2.print_info()

cubik = Cube((12,12,12),5,True)
cubik.print_info()
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
