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

    def fair_tournament(self):
        finishers = {}
        place = 1
        while self.participants:
            winners = []
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    winners.append(participant)
            while winners:
                max_distance = self.full_distance
                ind_best = 0
                for ind in range(len(winners)):
                    if winners[ind].distance > max_distance:
                        ind_best = ind
                        max_distance = winners[ind].distance
                finishers[place] = winners[ind_best]
                self.participants.remove(winners[ind_best])
                winners.remove(winners[ind_best])
                place += 1
        return finishers
