# Модифицировал калькулятор, добавил: основной код обернул в функцию, добавил повторение работы

from colorama import init
from colorama import Fore, Back, Style
init()


def computing():
    print(Fore.BLACK)
    print(Back.YELLOW)
    what = input("Что делаем? (+,-,*,/):")
    while True:
        if what not in "+-/*":
            print(Back.RED)
            print("Введено не верное значение!\nВведите значения + или - или * или /")
            what = input("Что делаем? (+,-,*,/):")
            continue
        else:
            break

    print(Back.GREEN)
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(Back.CYAN)
    if what == "+":
        print(f"Результат: {a + b}")
    if what == "-":
        print(f"Результат: {a - b}")
    if what == "*":
        print(f"Результат: {a * b}")
    if what == "/":
        print(f"Результат: {a / b}")


computing()

print(Back.BLUE)
again = input("Хотите продолжить вычисления?(д - да, н - нет): ")
while True:
    if again == "д":
        computing()
    if again == "н":
        print("Если нужно будет что-то посчитать, возвращайтесь")
        break
    else:
        print("Вводите только 'д' что означает да или 'н' что означает нет ")
        again = input("Хотите продолжить вычисления?(д - да, н - нет): ")
        continue





