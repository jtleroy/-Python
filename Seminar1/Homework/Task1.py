print("Ты начинаешь свой нелегкий путь изучения языка Python. Хочется узнать тебя лучше].")
name = input("Введи свое имя: ")
print('Приветствую тебя,' + name + '. У тебя очень красивое имя =)')
age = int(input('Сколько тебе лет? '))
if age < 20:
    print("Ты так молод, но уже решился изучать Python! Ты большой молодец")
elif age < 50 and age > 30:
    print("Очень хороший возраст для изучения нового")
else:
    print("Ого! ничего себе! так долго живут!")

print(name + 'Приветствую тебя,')
print(name)
print(age)
print("hello, {}".format(name))