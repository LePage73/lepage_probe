# Домашнее задание по теме "Блокировки и обработка ошибок"

import threading
import random
import time

class Bank():

    def __init__(self, start_balance, lock_):
        self.balance = start_balance
        self.lock_ = lock_
        self.oper_deposit_ = 0
        self.oper_take_ = 0

    def deposit(self):
        if self.oper_deposit_ < 100:
            add_ = random.randint(50, 500)
            self.balance += add_
            print(f'Пополнение: {add_} руб. Баланс: {self.balance} руб.')
            # print(self.lock_.locked(), self.balance)
            if self.balance >= 500 and self.lock_.locked():
                self.lock_.release()
            time.sleep(0.01)
            self.oper_deposit_ += 1
            self.deposit()
        else:
            return

    def take(self):
        if self.oper_take_ < 100:
            sub_ = random.randint(50, 500)
            print(f'Запрос на снятие {sub_}')
            if sub_ <= self.balance:
                self.balance -= sub_
                # print(self.lock_.locked(), self.balance)
                print(f'Снятие: {sub_} руб. Баланс: {self.balance}')
            else:
                # print(self.lock_.locked(), self.balance)
                print('Запрос отклонён, недостаточно средств')
                self.lock_.acquire()
            self.oper_take_ += 1
            self.take()
        else:
            return
lock_ = threading.Lock()
bank_ = Bank(0, lock_)

take_ = threading.Thread(target=Bank.take, args=(bank_,))
deposit_ = threading.Thread(target=Bank.deposit, args=(bank_,))

take_.start()
deposit_.start()

deposit_.join()
take_.join()

print(f'Итоговый баланс: {bank_.balance}')

print(f'Число операций снятия: {bank_.oper_take_}, внесения: {bank_.oper_deposit_}')
