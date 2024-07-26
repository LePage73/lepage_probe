# Самостоятельная работа по уроку "Рекурсия"

def get_multiplied_digits(number):
    last_digit = number % 10
    while last_digit == 0 and number > 0: # отбрасываем 0
        number = int(number / 10)
        last_digit = number % 10
    print('На стек положим ', last_digit)
    if number == 0 or number == 1:
        return 1
    else:
        return get_multiplied_digits(int(number/10)) * last_digit

number = int(input('ВВедите целое число :'))
print('Произведение цифр числа (не включая 0):',get_multiplied_digits(number))