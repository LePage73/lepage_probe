# Домашнее задание по теме "Создание исключений"

class Car():
    def __init__(self,model,vin,numbers):
        self.model = model
        if self.__is_valid_vin(vin): self.__vin = vin
        if self.__is_valid_numbers(numbers): self.__numbers = numbers
    def  __is_valid_vin(self,vin_number): # raise
        if not isinstance(vin_number,int): raise IncorrectVinNumber(f'Неверный тип данных "{vin_number}"')
        if vin_number < 1000000: raise IncorrectVinNumber(f'Недостаточно цифр в "{vin_number}"')
        if vin_number > 9999999: raise IncorrectVinNumber(f'Слишком много цифр в "{vin_number}"')
        return True
    def __is_valid_numbers(self,numbers):
        if not isinstance(numbers,str): raise IncorrectCarNumbers(f'Некорректный тип данных "{numbers}"')
        if len(numbers) !=6: raise IncorrectCarNumbers(f'Неверная длина номера "{numbers}"')
        return True



class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message
class IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message = message


######################################################################
# Проверка по заданию
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'1. {first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'2. {second.model} успешно создан')

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'3. {first.model} успешно создан')

try:
  second = Car('Model2', 31234567891, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'4. {second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'5. {third.model} успешно создан')

