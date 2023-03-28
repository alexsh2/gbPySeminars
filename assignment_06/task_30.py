# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

import functions
import messages

term = functions.validateNumInput("Введите первый элемент прогрессии: ", messages.msg2)
diff = functions.validateNumInput("Введите шаг прогрессии: ", messages.msg2)
num = functions.validateNumInput("Введите количество элементов прогрессии: ", messages.msg2)
ap = list()
count = 0
for i in range(num):
    ap.append(term + (count) * diff)
    count += 1

print(f"\nАрифметическая прогрессия числа {term} с шагом {diff}:\n{ap}")
