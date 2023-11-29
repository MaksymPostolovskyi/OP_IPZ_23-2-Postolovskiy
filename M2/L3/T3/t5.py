'''
Бонусне завдання. 
Придумайте свою гру-загадку! 
Не соромтеся експериментувати з тими командами, які Ви вже знаєте!
Обов'язково придумайте і використовуйте свою власну ідею! 
'''

import random

def game():
    secret_number = random.randint(1, 10)
    attempts = 3

    print("Вітаю в грі-загадці!")
    print("Я загадав число від 1 до 10. Спробуйте вгадати!")

    while attempts > 0:
        guess = int(input("Ваша відповідь: "))

        if guess == secret_number:
            print("Вітаю! Ви вгадали!")
            break
        else:
            attempts -= 1
            print(f"Не вгадали! Залишилося спроб: {attempts}")

    else:
        print(f"На жаль, ви не вгадали. Загадане число було {secret_number}.")

game()
