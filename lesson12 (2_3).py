# Стиль кода часть II. Цикл While
list_ = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# первый вариант без break и continue
print ('Первый вариант')
i = 0
while list_[i] >= 0 and i < len(list_):
    print(list_[i])
    i += 1

# второй вариант
print ('Второй вариант')
list_ = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

while True :
    if list_[0] >= 0 :
        print(list_.pop(0))
        if len(list_) > 0 : continue
    break