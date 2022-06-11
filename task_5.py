var_a = int(input("Введите значение выручки "))
var_b = int(input("Введите значение издержек "))
if var_a > var_b:
    profit = var_a - var_b
    emp_count = int(input("Введите количество сотрудников"))
    rent = var_a / var_b
    profit_per_emp = profit / emp_count
    print("Прибыль = " + str(profit))
    print("Рентабельность составила " + str(rent))
    print("Прибыль фирмы в расчёте на одного сотрудника составила = " + str(profit_per_emp))
else:
    print("Убыток")
