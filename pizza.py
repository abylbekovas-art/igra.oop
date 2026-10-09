import random

score = 0
customer = 1

while customer <= 10:
    print()
    print("🍕 Клиент", customer)
    print("Выберите пиццу:")
    print("1 — Маргарита")
    print("2 — Сырная")
    print("3 — Пицца с сосисками")

    order = random.randint(1, 3)

    choice = int(input("Ваш выбор (1-3): "))

    if choice == order:
        print("✅ Правильно! Заказ выполнен!")
        score += 1

    else:
        print("❌ Неправильно! Попробуйте в следующий раз.")

    customer += 1

print()
print("🎉 Рабочий день закончен!")
print("Вы правильно выполнили", score, "из 10 заказов.")

if score >= 8:
    print("🏆 Отличная работа!")
elif score >= 5:
    print("👍 Неплохо!")
else:
    print("😅 Нужно потренироваться!")