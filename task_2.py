var_a = int(input())
var_sec = var_a % 60
var_min = (var_a // 60) % 60
var_h = var_a // 3600
print(var_h, var_min, var_sec, sep = ':')