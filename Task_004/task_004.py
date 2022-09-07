# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# 
# вводимое с клавиатуры N считаем корректным ( >0 ), правильность не проверяем



import os
import random

# получить число с консоли
#   message - сообщение для пользователя
def get_int(message: str) -> int:
    return int(input(message))

# имя файла
FILE_NAME = 'file.txt'

## MAIN ##

os.system('cls')

print(os.getcwd())

# проверить есть ли файл
if(not os.path.exists(FILE_NAME)):
    print('Отсутствует файл позиций элементов!')
else:
    n_list =[]
    n = get_int('Введите значение N: ')
    for i in range(0, n):
        n_list.append(random.randint(-n,n))

    fl_pos = open(FILE_NAME, 'r')
    n_pos =  fl_pos.readlines()
    fl_pos.close()

    result = 1
    err_pos = 0
    for pos in n_pos:
        p = int(pos)
        # используем try-ex для избежания вылета по 'list index out of range'
        try:
            result *= n_list[p]
        except:
            err_pos += 1    # посчитаем неправильные индексы
    
    print(f'Исходный список: {n_list}')
    print(f'Произведение: {result}\nОшибочных индексов: {err_pos} ')
    

