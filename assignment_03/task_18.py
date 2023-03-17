# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число,
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X,
# выведите наименьший по величине.
#
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import functions
import messages
import numpy as num

msg = "Введите количество элементов в массиве: "
num1 = functions.validateNumInput(msg, messages.msg2)
rList = list(num.random.randint(low=1, high=25, size=num1))
print(f"Сгенерирован массив случайных чисел: \n {rList}")

msg = "Введите число для поиска: "
num2 = functions.validateNumInput(msg, messages.msg2)

maxNum = max(rList)
res = 0
if num2 > maxNum:
    res = maxNum
else:
    c1 = num2 - 1
    c2 = num2 + 1
    while c1 > 0 or c2 <= maxNum:
        if c1 in rList:
            res = c1
            break
        elif c2 in rList:
            res = c2
            break
        else:
            c1 -= 1
            c2 += 1
print(f"Ближайшее к {num2} значение: {res}")
