# Реализуйте алгоритм перемешивания списка.
#
# выполнение собственным перемешиванием

import random
import os

os.system('cls')

# размерность списка 
LIST_SIZE = 10
# подготовим упорядоченный список
num_list = []
for i in range(0, LIST_SIZE):
    num_list.append(i)

print(f'Начальный список:\t{num_list}')

# перемешаем список
for i in range(0, LIST_SIZE):
    new_pos = random.randint(0, LIST_SIZE-1)
    num_list[i], num_list[new_pos] = num_list[new_pos], num_list[i]

# новый список
print(f'Перемешанный список:\t{num_list}')