# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2 -> 4
import functions
import messages

n1 = functions.validateNumInput("Введите целое число а: ", messages.msg2)
n2 = functions.validateNumInput("Введите целое число b: ", messages.msg2)


def summa(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        if a > b:
            return summa(a + 1, b - 1)
        if b > a:
            return summa(a - 1, b + 1)


print(summa(n1, n2))
