'''
Напишіть програму, яка просить користувача ввести свій місяць і день народження. 
Потім ваша програма повинна повідомити знак зодіаку користувача як частину 
відповідного вихідного повідомлення.

Козеріг з 22 грудня по 19 січня
Водолій з 20 січня по 18 лютого
Риби з 19 лютого по 20 березня
Овен з 21 березня по 19 квітня
Телець з 20 квітня по 20 травня
Близнюки з 21 травня по 20 червня
Рак з 21 червня по 22 липня
Лев з 23 липня по 22 серпня
Діва з 23 серпня по 22 вересня
Терези з 23 вересня по 22 жовтня
Скорпіон з 23 жовтня по 21 листопада
Стрілець з 22 листопада по 21 грудня


'''



month = input("Введіть місяць народження: ").lower()
day = int(input("Введіть день народження: "))


if (month == "грудень" and day >= 22) or (month == "січень" and day <= 19):
    zodiac_sign = "Козеріг"
elif (month == "січень" and day >= 20) or (month == "лютий" and day <= 18):
    zodiac_sign = "Водолій"
elif (month == "лютий" and day >= 19) or (month == "березень" and day <= 20):
    zodiac_sign = "Риби"
elif (month == "березень" and day >= 21) or (month == "квітень" and day <= 19):
    zodiac_sign = "Овен"
elif (month == "квітень" and day >= 20) or (month == "травень" and day <= 20):
    zodiac_sign = "Телець"
elif (month == "травень" and day >= 21) or (month == "червень" and day <= 20):
    zodiac_sign = "Близнюки"
elif (month == "червень" and day >= 21) or (month == "липень" and day <= 22):
    zodiac_sign = "Рак"
elif (month == "липень" and day >= 23) or (month == "серпень" and day <= 22):
    zodiac_sign = "Лев"
elif (month == "серпень" and day >= 23) or (month == "вересень" and day <= 22):
    zodiac_sign = "Діва"
elif (month == "вересень" and day >= 23) or (month == "жовтень" and day <= 22):
    zodiac_sign = "Терези"
elif (month == "жовтень" and day >= 23) or (month == "листопад" and day <= 21):
    zodiac_sign = "Скорпіон"
elif (month == "листопад" and day >= 22) or (month == "грудень" and day <= 21):
    zodiac_sign = "Стрілець"
else:
    zodiac_sign = "невідомий знак зодіаку"

print(f"Ваш знак зодіаку: {zodiac_sign}")
