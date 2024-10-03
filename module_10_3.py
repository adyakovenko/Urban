import threading
from threading import Thread
import random
import time


class Bank(Thread):
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        super().__init__()

    def deposit(self):
        for transaction_number in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            transaction_money = random.randint(50, 500)
            self.balance += transaction_money
            print(f"Пополнение: {transaction_money}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        transaction_money = random.randint(50, 500)
        print(f"Запрос на {transaction_money}")
        for transaction_number in range(100):
            if transaction_money <= self.balance:
                self.balance -= transaction_money
                print(f"Снятие: {transaction_money}. Баланс: {self.balance}")
                time.sleep(0.001)
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


if __name__ == '__main__':
    bk = Bank()
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(f'Итоговый баланс: {bk.balance}')
