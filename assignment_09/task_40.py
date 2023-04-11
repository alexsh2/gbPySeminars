# Задача 40: Работать с файлом california_housing_train.csv,
# который находится в папке sample_data. Определить среднюю стоимость дома,
# где кол-во людей от 0 до 500 (population).
import pandas as pd
import numpy as np

df = pd.read_csv('california_housing_train.csv')
print(f"Минимальная цена дома: \t\t\t\t\t\t\t\t{df['medianHouseValue'].min()}")
print(f"Максимальная цена дома: \t\t\t\t\t\t\t{df['medianHouseValue'].max()}")
print(
    f"Средняя цена дома с проживанием до 500 человек: \t{np.round(df[df['population'] <= 500]['medianHouseValue'].mean())}")
print(
    f"Медианная цена дома с проживанием до 500 человек: \t{np.round(df[df['population'] <= 500]['medianHouseValue'].median())}")
