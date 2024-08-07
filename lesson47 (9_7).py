# Домашнее задание по теме "Декораторы"

def is_primes(func_):
    def wrapper(*args,**kwargs):
        value_ = func_(*args)
        if is_prime(value_):
            print('Простое')
        else:
            print('Составное')
        return value_

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return wrapper

@is_primes
def sum_three(*args):
    return args[0] + args[1] + args[2]

# Проверка по заданию
result = sum_three(2, 3, 6)
print(result)
result = sum_three(2, 4, 6)
print(result)

