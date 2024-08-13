import unittest

# Проверяемый класс Runner  ######################################
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

# Тест класса Runner ###########################################
class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_ = Runner('Test1')
        for _ in range(10): runner_.walk()
        self.assertEqual(runner_.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_ = Runner('Test2')
        for _ in range(10): runner_.run()
        self.assertEqual(runner_.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = Runner('1')
        runner_2 = Runner('2')
        for _ in range(10):
            runner_1.run()
            runner_2.walk()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

# Запуск проверки ###############################################

if __name__ == '__main__':
    unittest.main()
