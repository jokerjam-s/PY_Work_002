# Реализуйте алгоритм перемешивания списка.
#
# выполнение стандартными методами библиотеки random

import random
import os

os.system('cls')

# подготовим упорядоченный список
num_list = []
for i in range(0, 10):
    num_list.append(i)

print(f'Начальный список:\t{num_list}')

# перемешаем список
random.shuffle(num_list) 

# новый список
print(f'Перемешанный список:\t{num_list}')