'''
Виведіть площу виділеного червоним трикутника.

1) Запросіть два числа a і b - сторони прямокутника.
2) Зверніть увагу: площа червоного трикутника дорівнює половині площі намальованого прямокутника!
Відповідь має відповідати формату виведення, як вказано в прикладі. 
Формула знаходження площі  прямокутника S = a * b.
'''


a = float(input("Введіть довжину прямокутника (a): "))
b = float(input("Введіть ширину прямокутника (b): "))


S_rectangle = a * b


S_triangle = 0.5 * S_rectangle


print("S_triangle = {:.2f}".format(S_triangle))