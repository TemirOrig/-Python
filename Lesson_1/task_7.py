var_a = int(input("Расстояние за первый день "))
var_b = int(input("Расстоянние, которое необходимо пройти "))
i = var_a
day = 1
while i <= var_b:
    i = i * 1.1
    day += 1
print(day)
