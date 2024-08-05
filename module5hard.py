class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password and self.age == other.age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __ne__(self, other):
        return self.__eq__(other)

    def is_found(self, value):
        return value.lower() in self.title.lower()


import time


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __print__(self):
        print(self.current_user.nickname)

    def log_in(self, nickname, password, age):
        user = User(nickname, password, age)
        if user in self.users:
            self.current_user = user

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user.nickname in (user.nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(user)
            self.log_in(nickname, password, age)

    def log_out(self):
        self.current_user = None

    def add(self, *new_videos):
        for video in new_videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_title):
        return [video.title for video in self.videos if video.is_found(search_title)]

    def watch_video(self, search_title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if video.title == search_title:
                    if video.adult_mode is True and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        for t in range(video.time_now, video.duration):
                            time.sleep(1)
                            video.time_now += 1
                            print(video.time_now, end=' ')
                        print("Конец видео")
                        video.time_now = 0
                        break


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
