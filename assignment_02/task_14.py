# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

while True:
    num = input("Введите целое положительное число: ")
    if num.isdigit():
        break
    else:
        print("Введено не число. Повторите ввод")
p = 2
print("Степени двойки: ")
while p <= int(num):
    print(p, end=" ")
    p *= 2