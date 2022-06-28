
def gen_fact(num):
    fact_num = 1
    if num == 0:
        yield f'{num}! = 1'
    for i in range(1, num + 1):
        fact_num *= i
        yield f'{i}! = {fact_num}'


for el in gen_fact(int(input('Введите число: '))):
    print(el)
