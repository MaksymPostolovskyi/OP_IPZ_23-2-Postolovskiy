'''
Напишіть програму, яка починається з читання номіналу банкноти у користувача. 
Потім ваша програма повинна відобразити ім'я фізичної особи, 
яке фігурує на банкноті введеної суми. 
Відповідне повідомлення про помилку має відображатися, 
якщо такої банкноти немає.


'''

nominal = int(input("Введіть номінал банкноти: "))


if nominal == 1:
    person = "George Washington"
elif nominal == 2:
    person = "Thomas Jefferson"
elif nominal == 5:
    person = "Abraham Lincoln"
elif nominal == 10:
    person = "Alexander Hamilton"
elif nominal == 20:
    person = "Andrew Jackson"
else:
    person = "Немає такої банкноти"
    

print(f"Особа на банкноті {nominal} доларів: {person}")
