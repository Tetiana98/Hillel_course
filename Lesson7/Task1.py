#Task1
import os
import pandas as pd


dir_path = os.path.dirname(os.path.realpath('test_file.csv'))
file_path = os.path.join(dir_path, 'test_file.csv')
exchange_rate = 36
data = pd.read_csv(file_path)
for column in data:
    data[column] = data[column] * exchange_rate
    data.to_csv('salaries_uah.csv', index=False)

