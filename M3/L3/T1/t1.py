'''
Збережіть програму як модуль з ім'ям birthday.
Настав час створити свій перший модуль! 
Перед Вами програма, яка допомагає визначити, 
в яку пору року і в який день тижня народилася людина.
Збережіть її як модуль з ім'ям birthday і переходьте
до наступного завдання !
'''

# # Функція повертає рядок з назвою пори року, коли народилася людина


# def season(m):
#     if m < 3:
#         return "зима"
#     else:
#         if m < 6:
#             return "весна"
#         else:
#             if m < 9:
#                 return "літо"
#             else:
#                 if m < 12:
#                     return "осінь"
#                 else:
#                     return "зима"

# # Функція повертає рядок з назвою дня тижня, коли народилася людина


# def day(d):
#     if d == 1:
#         return "понеділок"
#     if d == 2:
#         return "вівторок"
#     if d == 3:
#         return "середа"
#     if d == 4:
#         return "четвер"
#     if d == 5:
#         return "п'ятниця"
#     if d == 6:
#         return "субота"
#     return "неділя"



def season(m):
    if m < 3:
        return "зима"
    elif m < 6:
        return "весна"
    elif m < 9:
        return "літо"
    elif m < 12:
        return "осінь"
    else:
        return "зима"


def day(d):
    if d == 1:
        return "понеділок"
    elif d == 2:
        return "вівторок"
    elif d == 3:
        return "середа"
    elif d == 4:
        return "четвер"
    elif d == 5:
        return "п'ятниця"
    elif d == 6:
        return "субота"
    else:
        return "неділя"


if __name__ == "__main__":
    m = int(input("Введіть номер місяця вашого народження: "))
    d = int(input("Введіть номер дня тижня вашого народження (1-7): "))
    
    s = "Ви народилися в пору року - {} і у день тижня - {}.".format(season(m), day(d))
    print(s)
