'''
Вільний діалог

Вільне завдання: вигадайте свою програму, яка задає питання і коментує відповіді.
Можна, наприклад, написати програму-анкету, яка запитує дані людини: ім'я, прізвище, вік, улюблені колір 
і страву і т. д., а потім друкує табличку типу 
"Ім'я: (ім'я людини)". 
"Прізвище: (введене прізвище)" 
і т. д.            
                                                                                  
А можна придумати смішний діалог. 
Запропонуйте друзям поговорити з цією програмою!
'''


name = input("Як вас звати? ")
age = input("Скільки вам років? ")
favorite_color = input("Який ваш улюблений колір? ")
favorite_food = input("Яка ваша улюблена страва? ")


print("-------------------------------")
print("Анкета:")
print(f"Ім'я: {name}")
print(f"Вік: {age} років")
print(f"Улюблений колір: {favorite_color}")
print(f"Улюблена страва: {favorite_food}")
print("-------------------------------")
print("Дякуємо за відповіді!")
