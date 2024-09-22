class Team:
    def __init__(self, name, score, time):
        self.name = name
        self.score = score
        self.time = time

    def __gt__(self, other):
        return self.score > other.score or (self.score == other.score and self.time < other.time)

    def __str__(self):
        return self.name

    def announce_victory(self):
        return f'Победа команды {self.name}!'




def percent_example_1val(n):
    print("В команде Мастера кода участников: %s ! " % n)



def percent_example_2val(n1, n2):
    print("Итого сегодня в командах участников: %s и %s !" % (n1, n2))


def format_example_score(score):
    print("Команда Волшебники данных решила задач: {} !".format(score))


def format_example_time(time):
    print("Волшебники данных решили задачи за {time} с !".format(time=time))


def f_string_example(score1, score2):
    print(f"Команды решили {score1} и {score2} задач.")

def f_string_example_challenge(challenge_result):
    print(f"Результат битвы: {challenge_result}!")


def f_string_example_tasks(n, t):
    print(f"Сегодня было решено {n} задач, в среднем по {t} секунды на задачу!.")


def get_result(team1, team2):
    if team1 > team2:
        return team1.announce_victory()
    if team2 > team1:
        return team2.announce_victory()
    return 'Ничья!'


def announce_winner(team1, team2):
    print(f"Результат битвы: {get_result(team1, team2)}")


if __name__ == '__main__':
    team1_num = 5
    team2_num = 6
    score_1 = 40
    score_2 = 42
    team1_time = 1552.512
    team2_time = 2153.31451
    tasks_total = 82
    time_avg = 45.2
    challenge_result = 'Победа команды Волшебники данных!'

    percent_example_1val(team1_num)
    percent_example_1val(team2_num)
    percent_example_2val(team1_num, team2_num)
    format_example_score(score_1)
    format_example_score(score_2)
    format_example_time(team1_time)
    format_example_time(team2_time)
    f_string_example(score_1, score_2)
    f_string_example_challenge(challenge_result)
    f_string_example_tasks(tasks_total, time_avg)

    team1 = Team('Мастера кода', score_1, team1_time)
    team2 = Team('Волшебники Данных', score_2, team2_time)
    announce_winner(team1, team2)

