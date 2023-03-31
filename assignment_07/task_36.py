# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.
#
# *Пример:*
#
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36
import functions
import messages

num_row = functions.validateNumInput("Введите количество строк: ", messages.msg2)
num_columns = functions.validateNumInput("Введите количество столбцов: ", messages.msg2)


def rows(r, c):
    row = list(map((lambda x: r * (x + 1)), range(c)))
    return row


def print_operation_table(op, num_rows=6, num_columns=6):
    r = 1
    while r <= num_rows:
        print(*op(r, num_columns))
        r += 1


print("\nТаблица:")
print_operation_table(rows, num_row, num_columns)
