from googletrans import Translator

translator = Translator()

with open('text_4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        num_1, num_2 = (i for i in line.split(' - '))
        translation = translator.translate(num_1, dest='ru')
        with open('text_4_1.txt', 'a', encoding='utf-8') as f_1:
            f_1.write(f'{translation.text} - {num_2}')
new_file = open('text_4_1.txt', 'r', encoding='utf-8')
print(*new_file)
new_file.close()
