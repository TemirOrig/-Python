class Cell:
    cells_count = "Количество ячеек в клетке"
    rows = 'Количество ячеек в строке'
    cell_name = 0

    def __init__(self, cells_count, rows):
        Cell.cell_name += 1
        self.cells_count = cells_count
        self.rows = rows

    def __str__(self):
        if Cell.cell_name == 1 or Cell.cell_name == 2:
            return f'Клетка - предок {Cell.cell_name}: Всего ячеек - {self.cells_count}| Максимум ячеек в строке' \
                   f' - {self.rows}'
        else:
            return f'Клетка - потомок {Cell.cell_name - 2}: Всего ячеек - {self.cells_count}' \
                   f'  | Максимум ячеек в строке - {self.rows}'

    def __add__(self, other):
        return Cell(self.cells_count + other.cells_count, self.rows + other.rows)

    def __sub__(self, other):
        if not self.cells_count > other.cells_count:
            raise ValueError('Разность ячеек клеток меньше или равна 0')
        else:
            return Cell(self.cells_count - other.cells_count, self.rows)

    def __mul__(self, other):
        return Cell(self.cells_count * other.cells_count, self.rows)

    def __truediv__(self, other):
        return Cell(round(self.cells_count / other.cells_count), self.rows)

    def make_order(self):
        i = '*' * self.rows
        k = self.cells_count
        while k >= self.rows:
            k -= self.rows
            print(f'{i}')
        else:
            i = '*' * (self.cells_count % self.rows)
            print(f'{i}\n')


cell_1 = Cell(8, 3)
print(cell_1)
cell_2 = Cell(7, 4)
print(cell_2)
cell_3 = cell_1 + cell_2
print(cell_3)
cell_3.make_order()
cell_4 = cell_1 - cell_2
print(cell_4)
cell_4.make_order()
cell_5 = cell_1 * cell_2
print(cell_5)
cell_5.make_order()
cell_6 = cell_1 / cell_2
print(cell_6)
cell_6.make_order()
