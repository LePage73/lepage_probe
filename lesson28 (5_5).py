# Дополнительное практическое задание по модулю 5

from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def login(self, nickname, password):
        for user_ in self.users:
            if nickname == user_.nickname:
                if hash(password) == user_.password:
                    self.current_user = user_
                    print(f'{self.current_user.nickname} вход выполнен')
                    return
                else:
                    print('Пароли не совпадают!!!')
                    return
        print('Пользователь не найден!!!')
        return

    def register(self, nickname, password, age):
        if len(self.users) == 0:
            if password != None and age != None:
                self.users.append(User(nickname, password, age))
                self.current_user = self.users[-1]
                print(f'Пользователь {nickname} успешно зарегистрирован')
            else:
                print('Введены не все данные')
                return
        else:
            for user_ in self.users:
                if nickname == user_.nickname :
                    print(f'Пользователь {nickname} уже существует')
                    return
                else:
                    self.users.append(User(nickname,password,age))
                    self.current_user = self.users[-1]
                    print(f'Пользователь {nickname} успешно зарегистрирован')
                    return
        return

    def log_out(self):
        self.current_user = None
        return

    def add(self, *video_list): # список классов Video на входе
        for video in video_list:
            video_appled = True
            for video_exist in self.videos:
                if str(video_exist.title).lower() == str(video.title).lower():
                    video_appled = False
                    print(f'Такое видео есть!" {video_exist.title}"')
            if  video_appled:
                self.videos.append(video)
        return

    def get_videos(self, search_word):
        video_list = []
        for video in self.videos:
            if str(search_word).lower() in str(video.title).lower():
                video_list.append(video.title)
        return video_list

    def watch_video(self, video_title):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.get_videos(video_title):
            for video_obj in self.videos:
                if video_obj.title == video:
                    if self.current_user.age < 18 and video_obj.adult_mode == True:
                      print(f'{self.current_user.nickname} нет 18 лет, "{video}" показан не будет')
                      continue
                    print(f'Показывается видео "{video}"')
                    print('Старт видео ', end ='' )
                    for cadre in range(video_obj.time_now, video_obj.duration+1):
                        print(cadre, end =' ')
                        sleep(0.3)
                    print('Конец видео')
                    continue
        return
# МОИ ТЕСТЫ
# проверка регистрации и входа
ur = UrTube()
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.register('urban', 'iScX4vIJzzClb9YQavjAgF', 25)
ur.login('vasya_pupkin', 'lolkekchebur')
print('Текущий пользователь: ',ur.current_user)

ur.login('vasya_pupkin', 'lolkekcheburek')

print('Текущий пользователь: ',ur.current_user)
ur.log_out()
# все вышли


# добавление видео
v1 = Video('Лучший язык программирования 2024 года', 20,3)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший ЯЗЫК программирования 2024 ГОДА', 20)
v4 = Video('Лучший стрелок',30,5,True)
ur.add(v1, v2, v2, v4)

# поиск видео
print(ur.get_videos('лучший'))
print(ur.get_videos('ЧЕГО'))

# просмотр видео
# я немного изменил задание точного соответствия не требуется
ur.login('vasya_pupkin', 'lolkekcheburek')
print('Текущий пользователь: ',ur.current_user)
ur.watch_video('лучший')
ur.login('urban', 'iScX4vIJzzClb9YQavjAgF')
print('Текущий пользователь: ',ur.current_user)
ur.watch_video('Чего')

# ТЕСТЫ ПО ЗАДАНИЮ
print('----------------------------------------------------------------')

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.login('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
