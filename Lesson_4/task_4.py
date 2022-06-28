source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
d = {}
for j in source_list:
    if j in d:
        d[j] += 1
    else:
        d[j] = 1
result = [item for item in source_list if d[item] == 1]
print(result)
