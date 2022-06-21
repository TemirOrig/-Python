def my_func(arg1, arg2, arg3):
    sorted_list = list([arg1, arg2, arg3])
    sorted_list.sort(reverse=True)
    print(sorted_list[0]+sorted_list[1])


my_func(int(input()), int(input()), int(input()))
