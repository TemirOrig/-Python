import numpy


with open('text_5.txt', 'w', encoding='utf-8') as f:
    ran_int_arr = numpy.random.randint(1, 100, 5)
    for el in ran_int_arr:
        f.write(f'{el} ')
    print(ran_int_arr.sum())
