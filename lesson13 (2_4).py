#Цикл for. Элементы списка. Полезные функции в цикле

numbers = [3, 2, 1, 4, 5, 6, 8, 7, 9, 10, 11, 19, 13, 14, 15]
# !!!! Программа оптимизирована для любого исходного набора чисел !!!!!!!!!!
is_prime = []
primes = []
not_primes = []

for i in list(range(len(numbers))) : # расставляем флаги
    is_prime.append(True) # изначально считаем простым пока дальше не докажем обратное
    if numbers[i] == 1 : # 1 - ни то, ни сё
        is_prime[i]=False
        continue
    if numbers[i] % 2 == 0 and numbers[i] != 2: # четное но не 2
        is_prime[i]=False
        continue
    else :
        for j in list(range(2, numbers[i])) : # проверяем делится ли на все предыдущие начиная с 3 (на 2 уже проверили)
            if numbers[i] % j == 0 : # если делится на предыдущее ставим флаг
                is_prime[i]=False
                break
for i in list(range(len(numbers))) : # разносим по спискам  зависимости от флага
    if numbers[i] == 1 : continue
    if is_prime[i] :
        primes.append(numbers[i])
    else :
        not_primes.append(numbers[i])
print(is_prime)
print(primes)
print(not_primes)