from random import *


answer = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определенно да", "Можешь быть уверен в этом",
          "Мне кажется-да", "Вероятней всего", "Хорошие перспективы", "Знаки говорят-да", "Да",
          "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
          "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ-нет", "По моим данным-нет",
          "Перспективы не очень хорошие", "Весьма сомнительно"]


print("Привет Друг, я магический шар, и я знаю ответ на любой твой вопрос.")
NAME = input("Как твое имя: ")
print(f"Привет {NAME}")

return_game = "д"

while return_game == "д":
    question = input("Введи свой вопрос: ")
    print(choice(answer))
    return_game = input("У тебя остались еще вопросы(д = да, н = нет) ?: ").lower()

    if not return_game == "д":
        print("Если возникнут вопросы возвращайся, буду рад на них ответить")