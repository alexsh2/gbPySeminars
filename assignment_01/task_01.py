# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример:
#         123 -> 6 (1 + 2 + 3)
#         100 -> 1 (1 + 0 + 0)


import messages
import functions

digits = 3
msg1 = f"Введите {digits}-значное число: "
inp = functions.validateNumInput(msg1, messages.msg2, messages.msg3, digits)
number = [int(i) for i in str(inp)]
sum = 0
for i in number:
    sum += i
print(f"Сумма цифр введённого числа {inp}: {sum}")
