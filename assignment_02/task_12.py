# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Дляэтого Петя делает две подсказки. Он называет сумму этих чисел S
# и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 2 2 -> 4 4
# 2 3 -> 5 6

import numpy as num
from sympy import sqrt

# Пете лень считать в уме.
res = list(num.random.randint(low=1, high=1000, size=2))

s = res[0] + res[1]
p = res[0] * res[1]
print(f"Петины числа: {res[0]}, {res[1]}")
print(f"Сумма двух натуральных чисел, задуманных Петей: S = {s}")
print(f"Произведение этих же чисел: P = {p}")

# Катин ответ
num1 = (s - sqrt(s ** 2 - 4 * p)) / 2
num2 = s - num1
print(f"Катин ответ: {num1}, {num2}")