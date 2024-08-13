# Домашнее задание по теме "Логирование"

import logging
## настройку журнала делаем до импорта остальных библиотек тогда файл лога создается
## ссылка - https://translated.turbopages.org/proxy_u/en-ru.ru.712817ad-66bb3cbc-67f85341-74722d776562/https
# /stackoverflow.com/questions/20240464/python-logging-file-is-not-working-when-using-logging-basicconfig

logging.basicConfig(level=logging.INFO, filemode="w", filename="log_test_12_4.log",
                        encoding="utf-8", format="%(levelname)s :< %(asctime)s >: %(message)s \n-------")

import unittest

## ТЕСТИРУЕМЫЙ ПАКЕТ #############################################################################################

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только числом, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers



### TEST ################################################################################################

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner_ = Runner('Test1',speed= -1)
            for _ in range(10): runner_.walk()
            self.assertEqual(runner_.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner_ = Runner(23545, 5)
            for _ in range(10): runner_.run()
            self.assertEqual(runner_.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = Runner('1')
        runner_2 = Runner('2')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

##########################################################################################

if __name__ == '__main__':
    unittest.main()


