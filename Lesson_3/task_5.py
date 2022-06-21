def numbers_input():
    my_list = input().split()
    return my_list


def sum_numbers(*my_list):
    sum_var = 0
    while True:
        my_list = numbers_input()
        if '!' not in my_list:
            my_list = [int(item) for item in my_list]
            sum_var += sum(my_list)
            print(sum_var)
        else:
            sum_index = my_list.index('!')
            my_list = [int(item) for item in my_list[:sum_index]]
            sum_var += sum(my_list[:sum_index])
            print(sum_var)
            break


sum_numbers()
