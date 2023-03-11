# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# Пример:
# 385916 -> yes
# 123456 -> no
import functions
import messages

digits = 6  # Разрядность требуемого числа
msg = f"Введите {digits}-значное число: "
inp = functions.validateNumInput(msg, messages.msg2, messages.msg3, digits)
ticket = [int(i) for i in str(inp)]
sum1 = 0
sum2 = 0
size = len(ticket)
i = 0

while True:
    if i < size / 2:
        sum1 += ticket[i]
        i += 1
    elif i > (size / 2 - 1) and i < size:
        sum2 += ticket[i]
        i += 1
    else:
        break
print(sum1, sum2)
if sum1 == sum2:
    print("Поздравляю! Вам достался счастливый билет.")
else:
    print("В следующий раз точно повезёт.")
