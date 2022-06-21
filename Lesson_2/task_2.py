my_list = list(input().split())
print(my_list, "До")

k = 1
i = 0
for i in range(len(my_list) - 1):
    while i < len(my_list) - 1 and k < len(my_list):
        my_list[i], my_list[k] = my_list[k], my_list[i]
        i += 2
        k += 2
print(my_list, "После")
