import re
from googletrans import Translator


translator = Translator()

with open('text_6.txt', 'r', encoding='utf-8') as f:
    subj_d = {}
    for line in f:
        key = line.strip().split(':')[0]
        key = translator.translate(key, dest='ru')
        key = key.text.capitalize()
        value = re.findall('\d+', line)
        value = [int(el) for el in value]
        value = sum(value)
        subj_d[key] = value
print(subj_d, end=' ')
