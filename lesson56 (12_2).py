# Домашнее задание по теме "Методы Юнит-тестирования"
import unittest

#####################################################

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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

##############################################################################################

class Tour_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Tour_Test.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('№_1_10', 10)
        self.runner_2 = Runner('№_2_09', 9)
        self.runner_3 = Runner('№_3_03', 3)

    @classmethod
    def tearDownClass(cls):
        _ = [print(x, 'забег', k,'место:', z) for x, y in Tour_Test.all_results.items() for k, z in y.items()]

    def test_Tour1(self):
        tour_ = Tournament(90, self.runner_1, self.runner_3)
        res_ = tour_.start()
        Tour_Test.all_results[1] = res_
        self.assertTrue(res_[max([key  for key, _ in res_.items()])] == '№_3_03')
    def test_Tour2(self):
        tour_ = Tournament(90, self.runner_2, self.runner_3)
        res_ = tour_.start()
        Tour_Test.all_results[2] = res_
        self.assertTrue(res_[max([key  for key, _ in res_.items()])] == '№_3_03')
    def test_Tour3(self):
        tour_ = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        res_ = tour_.start()
        Tour_Test.all_results[3] = res_
        self.assertTrue(res_[max([key  for key, _ in res_.items()])] == '№_3_03')

    # В тесте ниже будет AssertionError:, из-за ошибки в алгоритме метода start()
    # если самый медленный бегун будет заявлен 1-м и дистанция не более его
    # удвоенной скорости, в первом же цикле он выходит на 1 место

    # def test_Tour4(self):
    #     tour_ = Tournament(6, self.runner_3, self.runner_2, self.runner_1)
    #     res_ = tour_.start()
    #     Tour_Test.all_results[4] = res_
    #     self.assertTrue(res_[max([key  for key, _ in res_.items()])] == '№_3_03')

if __name__ == '__main__':
    unittest.main()