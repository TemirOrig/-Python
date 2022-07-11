from abc import ABC, abstractmethod


class Clothes(ABC):
    expenses_count = 0

    def expenses(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size
        Coat.expenses_count += self.expenses

    def __str__(self):
        return f'Coat: size - {self.size}, expenses - {self.expenses}, '\
                f'Total fabric expenses {Coat.expenses_count:.02f}'

    @property
    def expenses(self):
        exp = self.size / 6.5 + 0.5
        return float(f'{exp:0.2f}')


class Costume(Clothes):

    def __init__(self, size):
        self.size = size
        Costume.expenses_count += self.expenses

    def __str__(self):
        return f'Costume: size - {self.size}, expenses - {self.expenses}, ' \
               f'Total fabric expenses {Costume.expenses_count:.02f}'

    @property
    def expenses(self):
        exp = self.size * 2 + 0.3
        return float(f'{exp:0.2f}')


cloth_1 = Coat(77)
print(cloth_1)
cloth_2 = Costume(142)
print(cloth_2)
cloth_3 = Coat(123)
print(cloth_3)
cloth_4 = Costume(202)
print(cloth_4)
