# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no
import functions
import messages

l = "Введите длину шоколадки в дольках: "
w = "Введите ширину шоколадки в дольках: "
s = "Сколько долек желаете отломить? "
chocolateLength = functions.validateNumInput(l, messages.msg2)
chocolateWidth = functions.validateNumInput(w, messages.msg2)
chocolateSquares = functions.validateNumInput(s, messages.msg2)

if chocolateSquares > chocolateLength * chocolateWidth:
    print("Не жадничайте! В шоколадке нет столько долек.")
elif chocolateSquares == chocolateLength * chocolateWidth:
    print("Так это же вся шололадка целиком!")
elif chocolateSquares % chocolateLength == 0 or chocolateSquares % chocolateWidth == 0:
    print("Можно. Ломайте.")
else:
    print("Так ломать шоколадку тётя Оля не разрешает.")
