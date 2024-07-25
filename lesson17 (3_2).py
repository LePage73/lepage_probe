# Домашняя работа по уроку "Способы вызова функции"
domen = ('.com', '.ru', '.net') # "список"/кортеж разрешенных доменов

def send_email(message, to_, from_ = 'lepage@simbirsk.ru'):
    global domen
    to_.lower()
    from_.lower()
    if '@' in to_:
        if to_.endswith(domen):
            if to_ == from_:
                print('Нельзя отправить письмо самому себе!') # сам себе
                return False
            elif from_ == 'lepage@simbirsk.ru'.lower() :
                print(f'Письмо успешно отправлено с адреса {from_} на адрес {to_}')
                return True
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {from_} на адрес {to_}')
        else:
            print(f'Невозможно отправить письмо с адреса {from_} на адрес {to_}') # нет домена или домен не в списке
            return False
    else :
        print(f'Невозможно отправить письмо с адреса {from_} на адрес {to_}') # нет собачки
        return False

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', from_='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.su', from_='lepage@simbirsk.su')
send_email('Напоминаю самому себе о вебинаре', 'lepage@simbirsk.ru', from_='lepage@simbirsk.ru')

print('Разрешено высылать письма на:', domen)