from functools import reduce

print(reduce(lambda a, b: a * b, [item for item in range(100, 1001, 2)]))



