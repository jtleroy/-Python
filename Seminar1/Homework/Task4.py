# Задание 4.
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.
# Пример:
# Введите выручку фирмы: 1000
# Введите издержки фирмы: 500
# Финансовый результат - прибыль. Ее величина: 500
# Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
# Рентабельность выручки = 0.5
# Введите численность сотрудников фирмы: 10
# Прибыль фирмы в расчете на одного сотрудника = 50.0

profit = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if profit < costs:
    print('Финансовый результат - убыток')
else:
    print('Финансовый результат - прибыль')

financial_result = profit - costs
return_on_sales = profit/costs
print('Величина прибыли = {}, Рентабельность выручки {}'
      .format(financial_result, round(return_on_sales, 3)))
employees = int(input('Введите количество сотрудников: '))
profit_employees = financial_result/employees
print('Прибыль фирмы в расчете на одного сотрудника = ', profit_employees)