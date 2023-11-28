'''
Динамічний текст
Перетвори наявний текст в динамічний, який можна змінювати всередині коду за допомогою методу format. Текст можна розширити і доповнити самостійно, за бажанням.
'''

print("Привіт, Марк! Як ти себе почуваєш? Як твій настрій?")

name = "Марк"
mood = "щасливий"

text_template = "Привіт, {}! Як ти себе почуваєш? Як твій настрій?"

formatted_text = text_template.format(name)
print(formatted_text)


new_name = "Анна"
new_mood = "розуміючий"

new_formatted_text = text_template.format(new_name)
print(new_formatted_text)
