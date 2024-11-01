import unittest
import runner


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.runner_1 = runner.Runner('Усэйн', 10)
        self.runner_2 = runner.Runner('Андрей', 9)
        self.runner_3 = runner.Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def test_tournament_1(self):
        self.all_results['Турнир 1'] = runner.Tournament(90, self.runner_1, self.runner_3).start()
        self.assertTrue(self.all_results['Турнир 1'][len(self.all_results['Турнир 1'])].name == 'Ник')

    def test_tournament_2(self):
        self.all_results['Турнир 2'] = runner.Tournament(90, self.runner_2, self.runner_3).start()
        self.assertTrue(self.all_results['Турнир 1'][len(self.all_results['Турнир 1'])].name == 'Ник')

    def test_tournament_3(self):
        self.all_results['Турнир 3'] = runner.Tournament(90, self.runner_1, self.runner_2, self.runner_3).start()
        self.assertTrue(self.all_results['Турнир 1'][len(self.all_results['Турнир 1'])].name == 'Ник')

    def test_tournament_participants_order(self):
        self.assertTrue(runner.Tournament(21, self.runner_2, self.runner_1).start()[1].name == 'Усэйн')

    def test_fair_tournament_participants_order(self):
        self.assertTrue(runner.Tournament(21, self.runner_2, self.runner_1).fair_tournament()[1].name == 'Усэйн')

    @classmethod
    def tearDownClass(cls):
        for tournament, records in cls.all_results.items():
            print(f'{tournament}:')
            for stage, participant in records.items():
                print(f'Место {stage}: {participant.name}, (скорость {participant.speed})')
            print()


if __name__ == '__main__':
    unittest.main()
