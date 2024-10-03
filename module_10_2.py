from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f"{self.name}, на нас напали!")
        n_of_enemies = 100
        days = 0
        while n_of_enemies > 0:
            days += 1
            n_of_enemies = max(n_of_enemies - self.power, 0)
            time.sleep(1)
            print(f"{self.name} сражается {days} {self.say_day(days)}, осталось {n_of_enemies} воинов.")
        print(f"{self.name} одержал победу спустя {days} {self.say_day(days)}!")

    @staticmethod
    def say_day(n):
        if str(n)[-1] == '1':
            return 'день'
        if str(n)[-1] in ['2', '3', '4']:
            return 'дня'
        return 'дней'


if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    first_knight.join()
    second_knight.start()
    second_knight.join()
