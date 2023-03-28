# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
import numpy

import functions
import messages

count1 = functions.validateNumInput("Введите количество элементов первого множества: ", messages.msg2)
list1 = list(numpy.random.randint(low=0, high=20, size=count1))
set1 = set(list1)
count2 = functions.validateNumInput("Введите количество элементов второго множества: ", messages.msg2)
list2 = list(numpy.random.randint(low=0, high=20, size=count2))
set2 = set(list2)

print("Первый массив случайных целых чисел: ")
for item in list1:
    print(item, end=" ")
print()
print("Второй массив случайных целых чисел: ")
for item in list2:
    print(item, end=" ")
print()
temp = set1 & set2
res = sorted(temp)
print("Уникальные числа, входящие в оба массива, в порядке возрастания: ")
for item in res:
    print(item, end=" ")
