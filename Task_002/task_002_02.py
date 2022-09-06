# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#

# Вариант решения с помощью строки

import os

# получить число с консоли
#   message - сообщение для пользователя
def get_int(message: str) -> int:
    return int(input(message))


## MAIN ##
os.system('cls')

n = get_int('Введите число (>0) : ')

strk = '[1,'
proizv = 1
for i in range(2, n):
    proizv *= i
    strk += f' {proizv},'
strk += f' {proizv*n}]'

print(strk)