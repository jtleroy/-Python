# Задание 3.
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.#
# Пример:
# Введите число n: 3
# n + nn + nnn = 369

number = input('Введите число: ')
array = [number, number + number, number+number+number]
print(array[0], array[1], array[2])
a = int(array[0])
b = int(array[1])
c = int(array[2])
sum = a + b + c
print(sum)

