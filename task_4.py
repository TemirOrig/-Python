var_a = input()
ind_a = len(var_a) - 1
max = 0
i = 0
y = 0
while i < ind_a  and y < ind_a:
    if var_a[i] >= var_a[y + 1]:
        max = var_a[i]
        y += 1
    else:
        max = var_a[i + 1]
        i += 1
print(max)