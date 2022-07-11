class Matrix:

    def __init__(self, data):
        self.data = data
        for line in self.data[:-1]:
            if not len(line) == len(self.data[self.data.index(line) + 1]):
                raise ValueError('Разное количество элементов в строках')

    def __str__(self):
        return '\n'.join('\t'.join(str(num) for num in line) for line in self.data)

    def __add__(self, other):
        if not len(self.data) == len(other.data):
            raise ValueError('Размерности матриц не совпадают')
        else:
            for i in range(len(self.data)):
                if not len(self.data[i]) == len(other.data[i]):
                    raise ValueError('Размерности матриц не совпадают')
            item = [[int(self.data[line][num]) + int(other.data[line][num]) for num in
                     range(len(self.data[line]))] for line in range(len(self.data))]
            return Matrix(item)
