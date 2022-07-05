class Stationery:
    def __init__(self, title='Drawing instrument'):
        self.title = title

    def draw(self):
        print(f'Initialization of the "Risovach" protocol')


class Pen(Stationery):

    def draw(self):
        print(f'Unlocked new {self.title}...Pen PineApple PineApplePen')


class Pencil(Stationery):

    def draw(self):
        print(f"Unlocked new {self.title}...John Wick's pencil. Blood Eye Definitive Addition")


class Marker(Stationery):

    def draw(self):
        print(f"Unlocked new {self.title}... Just an ordinary marker. There is noting unusual")


station = Stationery()
station.draw()
pen = Pen('Avrora')
pen.draw()
pencil = Pencil('Koh-i-Noor')
pencil.draw()
marker = Marker('Potentate')
marker.draw()