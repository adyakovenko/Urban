import logging
import unittest
import traceback
import random
import runner

logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log", encoding='UTF-8', force=True,
                    format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """Test walk function"""
        try:
            test_subject = runner.Runner(str(random.random()), -1)
            for i in range(10):
                test_subject.walk()
            self.assertEqual(test_subject.distance, 50, "Runner.walk() doesn't work as expected")
            logging.info('"test_walk" выполнен успешно')
        except ValueError as error:
            logging.warning(f'Неверная скорость для Runner\n{traceback.format_exc()}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """Test run function"""
        try:
            test_subject = runner.Runner(name=[1,9, 2])
            for i in range(10):
                test_subject.run()
            self.assertEqual(test_subject.distance, 100, "Runner.run() doesn't work as expected")
        except TypeError as er:
            logging.warning(f"Неверный тип данных для объекта Runner\n{traceback.format_exc()}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """Test walk and run functions work differently"""
        test_subject_1 = runner.Runner(str(random.random()))
        test_subject_2 = runner.Runner(str(random.random()))
        for i in range(10):
            test_subject_1.run()
            test_subject_2.walk()
        self.assertNotEqual(test_subject_1.distance, test_subject_2.distance)


if __name__ == '__main__':
    unittest.main()
