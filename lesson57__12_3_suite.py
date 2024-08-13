# Домашнее задание по теме "Систематизация и пропуск тестов".

import unittest
import lesson57__12_3_RunnerTest as Runner_test
import lesson57__12_3_TourTest as Tour_test

derby_test_suite = unittest.TestSuite()

derby_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Runner_test.RunnerTest))
derby_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Tour_test.Tour_Test))

derby = unittest.TextTestRunner(verbosity=2)
derby.run(derby_test_suite)