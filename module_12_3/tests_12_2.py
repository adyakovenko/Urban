import unittest
import runner


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = runner.Runner('Усэйн', 10)
        self.runner_2 = runner.Runner('Андрей', 9)
        self.runner_3 = runner.Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        """Tournament 1"""
        self.all_results['Турнир 1'] = runner.Tournament(90, self.runner_1, self.runner_3).start()
        self.assertTrue(self.all_results['Турнир 1'][len(self.all_results['Турнир 1'])].name == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        """Tournament 2"""
        self.all_results['Турнир 2'] = runner.Tournament(90, self.runner_2, self.runner_3).start()
        self.assertTrue(self.all_results['Турнир 1'][len(self.all_results['Турнир 1'])].name == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        """Tournament 3"""
        self.all_results['Турнир 3'] = runner.Tournament(90, self.runner_1, self.runner_2, self.runner_3).start()
        self.assertTrue(self.all_results['Турнир 1'][len(self.all_results['Турнир 1'])].name == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_participants_order(self):
        """Tournament to break default code"""
        self.assertTrue(runner.Tournament(21, self.runner_2, self.runner_1).start()[1].name == 'Усэйн')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_fair_tournament_participants_order(self):
        """Fair tournament"""
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
