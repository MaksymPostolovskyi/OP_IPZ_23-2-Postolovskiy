'''
Виправте помилки в програмі. 
Програма повинна працювати так:
Спочатку отримати у людини очікуване число балів.
Після цього програма обчислює свій орієнтир: 
якщо число менше 50, то воно подвоюється. 
Якщо число більше або дорівнює 50, 
то орієнтиром буде число 100.
Також обирається, який текст надрукувати, 
в залежності від введеного числа. 
В результаті друкується цей текст і число. 
Наприклад, якщо введено 35, програма відповість: 
"А постарайтеся набрати 70 балів!". 
Якщо введено 70, програма відповість: 
"Давайте прагнути до максимуму: 100 балів!"

'''

# a = input "Скільки балів Ви розраховуєте набрати в цьому тесті?"
# if a < 50:
# a = 2 * a
# s = "А постарайтеся набрати "
# else:
#     a = 100
#     s = "Давайте прагнути до максимуму: "
#     print s + str(a) + " балів!"


a = int(input("Скільки балів Ви розраховуєте набрати в цьому тесті?"))


if a < 50:
    a *= 2
    s = "А постарайтеся набрати "
else:
    a = 100
    s = "Давайте прагнути до максимуму: "

print(s + str(a) + " балів!")

