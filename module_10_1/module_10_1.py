import time
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    fs = open(file_name, 'w', encoding='utf-16')
    for n in range(1, word_count + 1):
        fs.write(f"Какое-то слово № {n}\n")
        time.sleep(0.1)
    fs.close()
    print(f"Завершилась запись в файл {file_name}")


if __name__ == '__main__':
    t = datetime.now()
    args = ((10, 'example1.txt'), (30, 'example2.txt'), (200, 'example3.txt'), (100, 'example4.txt'))
    for i in range(len(args)):
        write_words(args[i][0], args[i][1])
    print(f'Работа потоков {datetime.now() - t}')
    t = datetime.now()
    threads = [Thread(target=write_words, args=args[i]) for i in range(len(args))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f'Работа потоков {datetime.now() - t}')
