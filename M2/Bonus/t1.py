'''
Напишіть програму, яка зчитує ціле число у користувача. 
Потім ваша програма повинна вивести повідомлення про те, 
парне чи непарне ціле число.

'''

number = int(input("Введіть ціле число: "))

if number % 2 == 0:
    print("Введене число є парним.")
else:
    print("Введене число є непарним.")
