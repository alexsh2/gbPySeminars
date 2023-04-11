#  Задание 44
# Ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
#
import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
lst += ['alien'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head(len(lst)))
print()
print(lst)
print()
print('index' + '\thuman' + '\trobot' + '\talien')
for i in range(len(lst)):
    if lst[i] == 'human':
        print(f'{i} \t\t1 \t\t0 \t\t0')
    elif lst[i] == 'robot':
        print(f'{i} \t\t0 \t\t1 \t\t0')
    else:
        print(f'{i} \t\t0 \t\t0 \t\t1')
