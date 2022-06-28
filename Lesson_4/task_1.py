import sys


def salary_calc():
    args = sys.argv[1:]
    args = [int(el) for el in args]
    print(f'{args[0] * args[1] + args[2]}')


salary_calc()
