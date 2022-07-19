from random import *

NAME = input("Имя в игре:")
print(f"Приветствую тебя{NAME} в игре 'Числовая угодайка'")


def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= num_random


num_random = int(input(f"Для начала игры ,{NAME} введите число, "
                       f"но помните чем больше число тем дольше мы будем играть;): "))


def game():
    number_random = randint(1, num_random)
    count = 0
    while True:
        enter_num = input(f"Введите число от 1 до {num_random} :")
        count += 1
        if is_valid(enter_num) is False:
            print(f"Не верное значение, введите число от 1 до {num_random}")
        if is_valid(enter_num) is True:
            enter_num = int(enter_num)
            if enter_num < number_random:
                print('Ваше число меньше загаданного, попробуйте еще разок:')
            elif enter_num > number_random:
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print(f"{NAME} Вы угадали за {count} попыток. Поздравляю Вас")
                break

    return_game = input("Хотите повторить игру:").lower()
    while return_game:
        if return_game in ("да", "д", "yes", "y"):
            game()
        else:
            print(f"{NAME} спасибо что играли в мою игру, надеюсь она Вам понравилась. До новых встреч")


game()





