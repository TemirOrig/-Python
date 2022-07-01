with open('text_3.txt', 'r', encoding='utf- 8') as f:
    names = []
    av_salary = 0
    num = 0
    for line in f:
        num += 1
        name, salary = (i for i in line.split())
        salary = float(salary)
        if salary < 20000:
            names.append(name)
        av_salary += salary
    av_salary /= num
print(*names, sep='| ')
print(f'Average salary: {av_salary}')
