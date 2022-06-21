def my_f(arg_1, arg_2):
    if arg_2 == 0:
        print("Деление на ноль недопустимо")
    else:
        return arg_1 / arg_2


print(my_f(int(input()), int(input())))

