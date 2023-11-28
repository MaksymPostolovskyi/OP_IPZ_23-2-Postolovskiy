'''
обмеження 15 рядків
Створіть програму, яка зчитує довжину та ширину поля фермера від користувача
у футах. Відобразити площу поля в акрах

TODO Hint: There are 43,560 square feet in an acre
'''


feet_per_acre = 43560

length = float(input("Введіть довжину поля у футах: "))
width = float(input("Введіть ширину поля у футах: "))

area_acres = (length * width) / feet_per_acre
print(f"Площа поля: {area_acres:.2f} акрів")
