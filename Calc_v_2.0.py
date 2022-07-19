
from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.BLACK)
print(Back.YELLOW)
what = input("Что делаем? (+,-,*,/):")

print(Back.GREEN)
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print(Back.CYAN)
if what == "+":
    c = a + b
    print("Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
if what == "*":
    c = a * b
    print("Результат: " + str(c))
elif what == "/":
    c = a / b
    print("Результат: " + str(c))

print(Back.MAGENTA)
input("Это моя первая работа.Ну как тебе калькулятор?")

print(Back.RED)
print("Большое спасибо за Ваш комментарий)))")



