# Задача 26:  Напишите программу, которая на вход принимает два числа A и B
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
import functions
import messages

base = functions.validateNumInput("Введите основание А: ", messages.msg2)
exponent = functions.validateNumInput("Введите показатель В: ", messages.msg2)


def power(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    elif exp < 0:
        return 1 / (base * power(base, -exp - 1))
    else:
        return base * power(base, exp - 1)


res = power(base, exponent)
print(f"{base} в степени {exponent} = {res}")
