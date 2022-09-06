# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
#

import os

# получить число с консоли
#   message - сообщение для пользователя
def get_int(message: str) -> int:
    return int(input(message))

## MAIN ##

os.system('cls')

n = get_int('Введите число: ')

# формируем список
list_number = []
for i in range(1, n+1):
    list_number.append((1 + 1/i)**i)

# подготовка к выводу результата в формате задачи
result = f'{n}: {{1:{list_number[0]}'
for i in range(1, n):
    result += f', {i+1}:{list_number[i]:.2f}'
result += '}'

print(result)