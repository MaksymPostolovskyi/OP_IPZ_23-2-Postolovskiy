'''
Напишіть програму, яка визначає ім'я фігури за кількістю сторін.
Прочитайте кількість сторін від користувача, 
а потім повідомте відповідне ім'я як частину змістовного повідомлення. 
Ваша програма повинна підтримувати фігури з будь-якого місця 
від 3 до 10 сторін (і включно). 
Якщо введено кілька сторін за межами цього діапазону, 
то ваша програма повинна видати відповідне повідомлення про помилку.

'''


num_sides = int(input("Введіть кількість сторін (від 3 до 10): "))


if 3 <= num_sides <= 10:
    if num_sides == 3:
        figure_name = "трикутник"
    elif num_sides == 4:
        figure_name = "четвертина"
    elif num_sides == 5:
        figure_name = "п'ятикутник"
    elif num_sides == 6:
        figure_name = "шестикутник"
    elif num_sides == 7:
        figure_name = "семикутник"
    elif num_sides == 8:
        figure_name = "восьмикутник"
    elif num_sides == 9:
        figure_name = "дев'ятикутник"