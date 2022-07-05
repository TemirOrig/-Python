class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'


cleaner = Position('Pavel', 'Ivanov', 'cleaner', 25000, 7000)
print(cleaner.get_full_name())
print(cleaner.position)
print(cleaner.get_total_income())
