from itertools import islice, count, cycle


def numbers_gen(st_el, fin_el, num_str):
    try:
        st_el, fin_el, num_str = int(st_el), int(fin_el), int(num_str)
        my_list = [el for el in islice(count(), st_el, fin_el + 1)]
        rep_list = iter(el for el in cycle(my_list))
        repeat_list = [next(rep_list) for _ in range(num_str)]
        print(my_list)
        return repeat_list
    except ValueError:
        return "ValueError"
    except TypeError:
        return "TypeError"


print(numbers_gen(input('Введите начальный элемент'), input('Введите конечный элемент'), input()))

