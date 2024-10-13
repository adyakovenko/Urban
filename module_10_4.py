import threading
from threading import Thread
import queue
import time
import random


class Table(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number
        self.guest = None
        self.serving = None

    def start_to_serve(self):
        self.serving = threading.Thread(target=self.guest.run)
        self.serving.start()


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randrange(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = [table for table in tables]

    def guest_arrival(self, *guests):
        for ind_guest in range(len(guests)):
            free_table_found = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guests[ind_guest]
                    table.start_to_serve()
                    free_table_found = True
                    print(f'{guests[ind_guest].name} сел(-а) за стол номер {table.number}')
                    break
            if free_table_found is False:
                for ind in range(ind_guest, len(guests)):
                    self.queue.put(guests[ind])
                    print(f'{guests[ind].name} в очереди')
                break

    def discuss_guests(self):
        while self.queue.empty() is False or any(table.name is True for table in self.tables):
            for table in self.tables:
                if table.serving.is_alive() is False:
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if self.queue.empty() is False:
                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.start_to_serve()


if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
