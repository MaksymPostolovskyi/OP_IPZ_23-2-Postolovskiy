'''
Вигадай свого супергероя.
Вигадай свого супергероя. Опиши його вміння, якості, силу, здібності і т. Д., І виведи опис на екран за допомогою функції print (). За допомогою методу format зроби опис динмічним. Не забувай, що весь текст повинен бути написаний всередині потрійних лапок.
'''
superhero_name = "Quantum Visionary"
superpower = "control over quantum particles"
strength = "superhuman strength"
ability = "time manipulation"
personality_trait = "calm and analytical"

superhero_description = """
Познайомтеся із {superhero_name}, супергероєм, який має надзвичайні здібності та сили!

{superhero_name} володіє {superpower}, що дозволяє йому контролювати квантові частинки. Його {strength} дозволяє йому виконувати неймовірні фізичні подвиги, але це лише одна з його багатьох неймовірних вмінь.

Найвражаюча з його здібностей - це {ability}. {superhero_name} може втручатися в текучість часу, роблячи його дії необхідними та точними. Ця унікальна здібність робить його непереможним у боротьбі з будь-якими загрозами.

Незвичайні сили поєднуються з {personality_trait} характером. {superhero_name} завжди залишається спокійним та аналітичним, знаходячи найкращі рішення навіть у найскладніших ситуаціях.

Приготуйтеся світ, {superhero_name} прийшов захищати вас!
"""

print(superhero_description.format(superhero_name=superhero_name, superpower=superpower, strength=strength, ability=ability, personality_trait=personality_trait))
