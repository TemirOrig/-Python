import time
from colorama import Fore, init
from datetime import datetime


init(autoreset=True)


def countdown(secs):
    while secs:
        # m, s = divmod(secs, 60)
        # time_format = '{:02d}:{02d}'.format(m, s)
        print(f'\r{secs}', end='')
        time.sleep(1)
        secs -= 1


class TrafficLight:
    __color = 'Private color'

    def __init__(self):
        self.col = None
        self.slp = None

    def running(self, text_c, sleep_tl=True):
        self.col = text_c
        self.slp = sleep_tl
        color_list = [Fore.RED, Fore.YELLOW, Fore.GREEN]
        sleep_list = [7, 2, 6]
        for self.col, self.slp in zip(color_list, sleep_list):
            datetime.now()
            print(f'\r{self.col + text_c}')
            countdown(self.slp)


a = TrafficLight()
a.running('*****')
print(a.col)
