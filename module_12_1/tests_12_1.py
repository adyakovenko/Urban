import unittest
import random

import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """Test walk function"""
        test_subject = runner.Runner(str(random.random()))
        for i in range(10):
            test_subject.walk()
        self.assertEqual(test_subject.distance, 50, "Runner.walk() doesn't work as expected")

    def test_run(self):
        """Test run function"""
        test_subject = runner.Runner(str(random.random()))
        for i in range(10):
            test_subject.run()
        self.assertEqual(test_subject.distance, 100, "Runner.run() doesn't work as expected")

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
