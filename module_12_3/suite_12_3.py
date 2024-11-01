import unittest
import tests_12_1
import tests_12_2

complex_suite = unittest.TestSuite()
complex_suite.addTest((unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest)))
complex_suite.addTest((unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest)))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(complex_suite)
