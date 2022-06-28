source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([j for i, j in zip(source_list, source_list[1:]) if j > i])

