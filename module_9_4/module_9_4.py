from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda f, s: f == s, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        fs = open(file_name, 'w', encoding='utf-16')
        for chunk in data_set:
            fs.write(f'{str(chunk)}\n')
        fs.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = [word for word in words]

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())