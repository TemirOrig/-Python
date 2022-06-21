def my_func(a, b):
    if a >= 0 and b < 0:
        print(f'{a ** b}')
    else:
        print("Введите корректные значения")


def my_func_alt(a, b):
    if a >= 0 and b < 0:
        i = -1
        z = 1
        while i >= b:
            z /= a
            i = i - 1
        print(z)
    else:
        print("Введите корректные значения")


x = int(input("Введите основание - положительное: "))
y = int(input("Введите степень числа - отрицательное, целое: "))

my_func(x, y)
my_func_alt(x, y)

