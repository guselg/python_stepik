direction = input('Выберите направление. ш - шифрование, д - дешифрование: ')
language = input('Укажите язык шифрования/дешифрования. ru/en ')
step = int(input('Укажите шаг сдвига: '))
phrase = input('Введите фразу: ')

alphabet = {
    'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя',
    'en': 'abcdefghijklmnopqrstuvwxyz'
}

resalt = ''
for i in range(len(phrase)):
    n_is_upper = phrase[i].isupper()
    if phrase[i].lower() in alphabet[language]:
        number_letter = alphabet[language].index(phrase[i].lower())
        if direction == 'ш':
            new_number_letter = number_letter + step
        elif direction == 'д':
            new_number_letter = number_letter - step
        if new_number_letter > len(alphabet[language])-1:
            new_number_letter = new_number_letter - len(alphabet[language])
            new_letter = alphabet[language][new_number_letter]
        elif new_number_letter <= len(alphabet[language])-1:
            new_letter = alphabet[language][new_number_letter]
        if n_is_upper:
            new_letter = new_letter.upper()
    else:
        new_letter = phrase[i]
    resalt += new_letter
print(resalt)

# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).

phrase = 'To be, or not to be, that is the question'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

word = ''
sphrase = ''


def shifr(word):
    step = len(word)
    new_word = ''
    for i in range(len(word)):
        number_letter = alphabet.index(word[i].lower())
        new_number_letter = number_letter + step
        if new_number_letter > len(alphabet) - 1:
            new_number_letter = new_number_letter - len(alphabet)
            new_letter = alphabet[new_number_letter]
        elif new_number_letter <= len(alphabet) - 1:
            new_letter = alphabet[new_number_letter]
        n_is_upper = word[i].isupper()
        if n_is_upper:
            new_letter = new_letter.upper()
        else:
            new_letter = new_letter
        new_word += new_letter
    return new_word


for i in range(len(phrase)):
    if phrase[i].lower() in alphabet:
        word += phrase[i]
    else:
        if len(word) > 0:
            sphrase += shifr(word)
            word = ''
        sphrase += phrase[i]
    if i == (len(phrase)-1):
        sphrase += shifr(word)
print(sphrase)

