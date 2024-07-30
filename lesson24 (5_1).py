# Домашняя работа по уроку "Атрибуты и методы объекта."

class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print(f'В {self.name} этажа с номером {new_floor} не существует')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 4)
h1.go_to(19)
h2.go_to(4)