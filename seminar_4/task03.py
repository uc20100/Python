# Задача 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов последовательности в том же порядке.  
# in -> 10  
# out -> [4, 4, 5, 5, 6, 2, 3, 8, 9, 4]  
# out -> [6, 2, 3, 8, 9] 

import random
MIN_VALUE_RANDOM = 0
MAX_VALUE_RANDOM = 9

input_string = input('Введите размер последовательности чисел: ')
while not input_string.isdigit():
    print('Ошибка ввода.')
    input_string = input('Введите размер последовательности чисел: ')

number_list = [random.randint(MIN_VALUE_RANDOM,MAX_VALUE_RANDOM) for i in range(int(input_string))]
result_list = [i for i in number_list if number_list.count(i)==1]
print(f'Список номеров                  -> {number_list}')
print(f'Список не повторяющихся номеров -> {result_list}')

