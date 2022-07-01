
with open('text_2.txt', 'r', encoding='utf-8') as f:
    lines = 0
    for line in f:
        res = line.split()
        lines += 1
        words = len(res)
        print(f'String №{lines}: {words} words')
print(f'Lines in total: {lines}')
