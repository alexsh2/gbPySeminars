# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
#
# Ввод: 5
# Ввод: 1
#
# 1 2 1 2 2
# Вывод: 2

import numpy as num
import functions
import messages
from collections import Counter

msg = "Введите количество элементов в массиве: "
num1 = functions.validateNumInput(msg, messages.msg2)
res = list(num.random.randint(low=1, high=5, size=num1))
print(f"Сгенерирован массив случайных чисел: \n {res}")
msg = "Введите число для поиска: "
num2 = functions.validateNumInput(msg, messages.msg2)

print(f"Число {num2} встречается в массиве {res.count(num2)} раз(а)")
# list.count медленно работает на больших массивах. Counter(list) - быстрее
print(f"Вывод с помощью Counter: {Counter(res)[num2]}")
