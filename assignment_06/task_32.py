# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Пример:
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import numpy
import functions
import messages

num = functions.validateNumInput("Введите количество элементов массива: ", messages.msg2)
inpList = list(numpy.random.randint(low=-20, high=20, size=num))
print(f"Сгенерирован массив случайных чисел: \n {inpList}")

span = list(numpy.random.randint(low=-20, high=20, size=2))
if span[0] > span[1]:
    span[0], span[1] = span[1], span[0]
print(f"Заданный диапазон чисел: \n {span}")

resList = list()
for i in range(len(inpList)):
    if inpList[i] >= min(span) and inpList[i] <= max(span):
        resList.append(i)

if resList != []:
    print(f"Список индексов чисел, принадлежащих заданному диапазону (включительно): {resList}")
else:
    print("Ни одно из чисел массива не входит в заданный диапазон")
