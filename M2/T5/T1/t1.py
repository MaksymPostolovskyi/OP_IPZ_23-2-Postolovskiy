'''
Використовуйте функцію print, щоб чат-бот сказав користувачеві: "Вітаю, людино!".
Зверніть увагу на розділові знаки.
'''
print("Вітаю, людино!")
print("Я твій чат-бот. Як справи?")
mood = input("Як твій настрій сьогодні? ")

if "щаслив" in mood.lower():
    print("Це чудово, я радію за тебе!")
elif "сумний" in mood.lower():
    print("Не переймайся, можливо, я зможу тебе розвеселити.")
else:
    print("Цікаво, що ти сьогодні відчуваєш.")

print("Я завжди тут, якщо тобі потрібна підтримка чи розмова. До побачення!")