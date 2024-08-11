#  Секундомер, для дальнейшей работы понадобится
from datetime import datetime
class Timer:
    def __init__(self, name):
        self.name = name
        self.start_time = 0
        self.stop_time = 0

    def start(self):
        self.start_time = datetime.now()
    def stop(self):
        self.stop_time = datetime.now()
    def __str__(self):
        return str(self.stop_time - self.start_time)
    def current_time(self):
        return str(datetime.now() - self.start_time)
    def print_curr_time(self):
        print(f'Таймер {self.name}, с момента старта прошло:{self.current_time()} ')
