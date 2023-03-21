# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из
# управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# Пример:
# 4 -> 1 2 3 4
# 9
import numpy

import functions
import messages

bushes = functions.validateNumInput("Введите количество кустов на грядке: ", messages.msg2)
gardenBed = {}
temp = 1
while temp <= bushes:
    gardenBed[temp] = numpy.random.randint(low=20, high=24)
    temp += 1
print("Количество ягод на каждом кусте грядки:")
print(gardenBed)
print()

amount = large = 0
result = {}
w = 0
for item in gardenBed:
    if item + 1 == bushes + 1:
        amount = gardenBed[item - 1] + gardenBed[item] + gardenBed[1]
    elif item - 1 == 0:
        amount = gardenBed[bushes] + gardenBed[item] + gardenBed[item + 1]
    else:
        amount = gardenBed[item - 1] + gardenBed[item] + gardenBed[item + 1]
    if amount == large:
        result[item] = amount
    elif amount > large:
        large = amount
        w = item

print(f"Максимальное количество ягод с трёх рядом растущих кустов: {large}")
print("Собрать столько ягод можно, расположив собирающий модуль напротив кустов: ")

print(f"№{w}", end=" ")
for item in result:
    if result[item] == large:
        print(f"№{item}", end=" ")
