'''
Напишіть програму, яка починається з читання буквеної оцінки від користувача. 
Потім ваша програма повинна обчислити та відобразити еквівалентну кількість 
балів оцінок. Переконайтеся, що програма створює відповідне повідомлення 
про помилку, якщо користувач вводить неприпустиму оцінку букв.

'''


grade = input("Введіть буквену оцінку: ").upper()


if grade == "A":
    points = 4.0
elif grade == "A-":
    points = 3.7
elif grade == "B+":
    points = 3.3
elif grade == "B":
    points = 3.0
elif grade == "B-":
    points = 2.7
elif grade == "C+":
    points = 2.3
elif grade == "C":
    points = 2.0
elif grade == "C-":
    points = 1.7
elif grade == "D+":
    points = 1.3
elif grade == "D":
    points = 1.0
elif grade == "D-":
    points = 0.7
elif grade == "F":
    points = 0.0
else:
    print("Помилка: неприпустима буквена оцінка")
    points = None


if points is not None:
    print(f"Еквівалентна кількість балів: {points}")
