'''
Програма повинна запитати "Який найпопулярніший колір у світі?".
Правильна відповідь - "синій" (всі букви маленькі). 
Якщо колір вірний, програма друкує "Вгадано!". 
У разі неправильного кольору друкує "Не вгадано! Спробуйте ще раз!" 
і знову пропонує ввести колір.


'''

yes = "Вгадав!"
no = "Не вгадав! Спробуй ще раз!"


correct_color = "синій"

while True:
    user_color = input("Який найпопулярніший колір у світі? ").lower()

    if user_color == correct_color:
        print("Вгадано!")
        break
    else:
        print("Не вгадано! Спробуйте ще раз.")
