from random import *

is_char = {
    'digits': '0123456789',
    'lowercase_letters': 'abcdefghijklmnopqrstuvwxyz',
    'uppercase_letters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'punctuation': '!#$%&*+-=?@^_'
}

new_is_char = {
    'digits': '0123456789',
    'lowercase_letters': 'abcdefghijklmnopqrstuvwxyz',
    'uppercase_letters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'punctuation': '!#$%&*+-=?@^_'
}


def generate_password(length, chars1):
    chars = ''
    while length != len(chars):
        is_keys = choice(chars1)
        new_n = choice(new_is_char[is_keys])
        if is_not_char == 'д':
            if new_n not in 'il1Lo0O':
                chars = chars + new_n
        else:
            chars = chars + new_n
    print('Ваш пароль: ', chars)


n = int(input('Укажите количество паролей (целым числом): '))

for i in range(n):
    is_len = int(input('Укажите длину пароля: '))
    is_digits = input(f'Включать ли в пароль символы {is_char["digits"]}? (д = да, н = нет): ')
    is_lowercase_letters = input(f'Включать ли прописные буквы {is_char["lowercase_letters"]}? (д = да, н = нет): ')
    is_uppercase_letters = input(f'Включать ли строчные буквы {is_char["uppercase_letters"]}? (д = да, н = нет): ')
    is_punctuation = input(f'Включать ли строчные буквы {is_char["punctuation"]}? (д = да, н = нет): ')
    is_not_char = input(f'Исключать ли неоднозначные символы il1Lo0O? (д = да, н = нет): ')

    if is_digits.lower() == 'н':
        del new_is_char["digits"]
    if is_lowercase_letters.lower() == 'н':
        del new_is_char["lowercase_letters"]
    if is_uppercase_letters.lower() == 'н':
        del new_is_char["uppercase_letters"]
    if is_punctuation.lower() == 'н':
        del new_is_char["punctuation"]

    generate_password(is_len, list(new_is_char.keys()))
