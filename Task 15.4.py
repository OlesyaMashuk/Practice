rus = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
eng = 'abcdefghijklmnopqrstuvwxyz'
nonliteral = '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~'
freq_words = {}
engword = ''
while True:
    filename = input('Ввведите имя текстового файла без расширения: ')
    if filename == '':
        print('Имя файла не может быть задано пустой строкой. Введите корректное значение')
    else:
        break
filename = filename + ".txt"
with open(filename, 'r', encoding='utf8') as file:
    text = file.read()
for c in nonliteral:
    text = text.replace(c,'')
text = text.lower()
splittedtext = text.split()
for word in splittedtext:
    if len(word)>3:
        if word in freq_words.keys():
            freq_words[word] += 1
        else:
            freq_words[word] = 1
    if word[0] in eng:
        #слово английское
        if len(word) > len(engword):
            engword = word

keys = list(freq_words.keys())
values = list(freq_words.values())
max = max(values)
word = keys[values.index(max)]

print(f'Cлово "{word}" длиной более 3-х букв встречается в тексте {max} раз(а)')
print(f'Самым длинным английским словом в тексте является "{engword}"')