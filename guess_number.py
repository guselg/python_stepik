from random import *

print('Добро пожаловать в числовую угадайку')


def is_border():
    try:
        n_user = input('Укажите правую границу для случайного выбора числа (от 1 до n) ')
        return n_user
    except ValueError:
        print('Не верно указана граница')


n1 = is_border()


def is_valid(number):
    if 1 <= number <= int(n1):
        return True
    else:
        return False


def is_input():
    n = randint(1, int(n1))
    attempt = 0
    while True:
        try:
            num_user = int(input('Введите число от 1 до ' + n1 + ' '))
            attempt += 1
            if is_valid(num_user):
                if num_user < n:
                    print('Ваше число меньше загаданного, попробуйте еще разок')
                elif num_user > n:
                    print('Ваше число больше загаданного, попробуйте еще разок')
                elif num_user == n:
                    print('Вы использовали', attempt, 'попыток.')
                    print('Вы угадали, поздравляем!')
                    user_out = input('Желаете сыграть еще раз? Введите да/нет ')
                    if user_out.lower() == 'да':
                        attempt = 0
                        is_border()
                        is_input()
                    else:
                        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                        break
            else:
                print('А может быть все-таки введем целое число ')
                continue
        except ValueError:
            print('А может быть все-таки введем целое число ')


is_input()
