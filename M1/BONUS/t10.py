'''
Розробити програму, яка зчитує у користувача чотиризначне ціле число 
і відображає суму його цифр. Наприклад, якщо користувач вводить 3141,
то ваша програма повинна відображати 3 + 1 + 4 + 1 = 9.

'''


number = int(input("Введіть чотиризначне ціле число: "))


digit1 = number // 1000
digit2 = (number % 1000) // 100
digit3 = (number % 100) // 10
digit4 = number % 10


sum_of_digits = digit1 + digit2 + digit3 + digit4


print(f"Сума цифр числа {number}: {digit1} + {digit2} + {digit3} + {digit4} = {sum_of_digits}")
