'''
Кількість секунд
кількість секунд у році.
Напишіть програму, яка рахує і друкує, скільки секунд в році, в якому 365 діб

Зверніть увагу:
1 рік = 365 днів
1 день = 24 години
1 година = 60 хвилин
1 хвилина = 60 секунд

(Перемножує кількість секунд в хвилині, хвилин в годині, годин у добі, діб у році).
'''


seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
days_per_year = 365


seconds_per_year = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_year


print(f"Кількість секунд у році: {seconds_per_year}")
