# Стиль кода часть II. Цикл While

list_ = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

while True :
    if list_[0] == 0 :
        list_.pop(0)
        continue
    if list_[0] > 0 :
        print(list_.pop(0))
        if len(list_) > 0 : continue
    break