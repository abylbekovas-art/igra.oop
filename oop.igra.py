import random


# Список персонажей: list
# Данные персонажей: dict
# Подсказки: tuple

characters = [
    {
        "name": "Алиса",
        "hints": ("Она любит читать книги", "Она очень любознательная")
    },
    {
        "name": "Боб",
        "hints": ("Он любит программирование", "Он работает с компьютером")
    },
    {
        "name": "Чарли",
        "hints": ("Он хорошо играет в футбол", "Он любит спорт")
    },
    {
        "name": "Джек",
        "hints": ("Он любит музыку", "Он умеет играть на гитаре")
    },
    {
        "name": "Гарри Поттер",
        "hints": ("Он учится в школе магии", "Его лучший друг — Рон")
    },
    {
        "name": "Губка Боб",
        "hints": ("Он живёт в подводном городе", "Его дом похож на ананас")
    },
    {
        "name": "Шрек",
        "hints": ("Он живёт на болоте", "Его лучший друг — Осёл")
    },
    {
        "name": "Эльза",
        "hints": ("Она умеет создавать лёд", "Она королева из «Холодного сердца»")
    },
    {
        "name": "Человек-паук",
        "hints": ("Он умеет лазать по стенам", "Он использует паутину")
    },
    {
        "name": "Барби",
        "hints": ("Она известна своим розовым стилем", "О ней снят известный фильм")
    },
    {
        "name": "Супермен",
        "hints": ("Он умеет летать", "Его слабость — криптонит")
    },
    {
        "name": "Микки Маус",
        "hints": ("Это мышонок в красных шортах", "Он известный персонаж Disney")
    },
    {
        "name": "Золушка",
        "hints": ("Она потеряла хрустальную туфельку", "Она отправилась на бал")
    },
    {
        "name": "Пикачу",
        "hints": ("Он умеет создавать электрические разряды", "Он жёлтый персонаж Pokémon")
    }
]


# Функция одного раунда
def play_round(round_number, used_characters):
    print(f"\n========== Раунд {round_number} из 10 ==========")

    # Выбираем ещё не использованного персонажа
    available = [
        character for character in characters
        if character["name"] not in used_characters
    ]

    character = random.choice(available)
    used_characters.add(character["name"])

    print("Подсказка:", character["hints"][0])

    while True:
        try:
            answer = input("Угадай персонажа: ").strip().casefold()

            if not answer:
                print("Ошибка! Введи имя персонажа.")
                continue

            if answer == character["name"].casefold():
                print("Правильно! Ты получил(а) 1 балл!")
                return 1
            else:
                print("Неправильно! Попробуй ещё раз.")
                print("Дополнительная подсказка:",
                      character["hints"][1])

        except (EOFError, KeyboardInterrupt):
            print("\nВвод прерван. Раунд завершён.")
            return 0


# Функция игры на 10 раундов
def play_game():
    score = 0
    used_characters = set()

    print("\nДобро пожаловать в игру «Угадай персонажа»!")
    print("Тебя ждут 10 раундов.")
    print("За каждый угаданный персонаж ты получишь 1 балл.")

    for round_number in range(1, 11):
        score += play_round(round_number, used_characters)

    # Итоговый результат
    print("\n" + "=" * 35)
    print("ИГРА ОКОНЧЕНА!")
    print(f"Твой результат: {score} из 10 баллов")

    if score == 10:
        print("Отлично! Все ответы правильные!")
    elif score >= 7:
        print("Очень хороший результат!")
    elif score >= 4:
        print("Хорошая попытка! Продолжай тренироваться!")
    else:
        print("Попробуй ещё раз и улучши результат!")

    print("=" * 35)


# Главное меню
def main():
    while True:
        print("\n====== ГЛАВНОЕ МЕНЮ ======")
        print("1. Начать игру")
        print("2. Выйти")

        try:
            choice = input("Выбери действие (1 или 2): ").strip()

            if choice == "1":
                play_game()
            elif choice == "2":
                print("Спасибо за игру! До встречи!")
                break
            else:
                print("Ошибка! Введи 1 или 2.")

        except (EOFError, KeyboardInterrupt):
            print("\nПрограмма завершена.")
            break


# Запуск программы
if __name__ == "__main__":
    main()