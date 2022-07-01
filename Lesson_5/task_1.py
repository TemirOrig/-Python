print("Введите данные для записи\nДля окончания ввода введите пустую строку")
with open('text_1.txt', 'w', encoding='utf-8') as rec_file:
    while (line := input('Введите строку: ')) != '':
        rec_file.write(f'{line}\n')
