# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
import numpy
import functions
import messages

msg = "Сыпь монеты на стол, да побольше. Сколько не жалко? "
coins = functions.validateNumInput(msg, messages.msg2)
if coins == 0:
    print("Ну и скряга! Ни одной монетки не кинул!")
elif coins == 1:
    print("Всего одна монетка. Переворачивать нечего.")
else:
    res = list(numpy.random.randint(low=0, high=2, size=coins))
    print(f"Монеты рассыпались следующим образом: {res}")
    heads, tails = 0, 0
    for i in res:
        if i == 0:
            tails += 1
        else:
            heads += 1

    if tails == 0:
        print("Выпали одни решки. Ничего не переворачиваем.")
    elif heads == 0:
        print("Выпали одни орлы. Переворачивать нечего.")
    elif tails < heads:
        print(f"Переворачиваем орлов, их меньше: {tails} из {coins}.")
    elif heads < tails:
        print(f"Переворачиваем решки, их меньше: {heads} из {coins}.")
    else:
        print(f"Орлов({tails}) и решек({heads}) выпало поровну. Бросим монетку? (да/нет):)")
        if functions.validateYesNo():
            rnd = randint(0, 1)
            if rnd == 0:
                print(f"{rnd} - переворачиваем орлов")
            else:
                print(f"{rnd} - переворачиваем решки")
        else:
            print("На \"нет\" и суда нет.")
