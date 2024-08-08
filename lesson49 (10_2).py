# Домашнее задание по теме "Потоки на классах"
from threading import Thread
from time import sleep

class Terminator(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.t6000 = 100
        self.days = 0
        self.war_continue = True

    def run(self):
        if self.war_continue:
            self._war()

    def _war(self):
        if self.days == 0: print(f'-- {self.name}, на нас напали t6000!')
        self.t6000 -= self.power
        self.days += 1
        sleep(1)
        print(f'-- {self.name} сражается {self.days} дней, осталось {self.t6000} "T6000".')
        if self.t6000 <= 0:
            print(f'-- {self.name} одержал победу спустя {self.days} дней(дня)')
            self.war_continue = False

        self.run()


thread = []
terminator1 = Terminator('Sarah Connor', 10)
terminator2 = Terminator('Kyle Reese', 20)
terminator3 = Terminator('John Connor', 15)

# while terminator1.war_continue or terminator2.war_continue:
terminator1.start()
terminator2.start()
terminator3.start()

terminator1.join()
terminator2.join()
terminator3.join()

print('Все битвы закончились!')



