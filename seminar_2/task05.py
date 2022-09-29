# Задача 5. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random

str = input('Введите размер списка: ')
while str.isdigit() == False:
    print('Введённые символы не являются натуральным числом')
    str = input('Введите размер списка: ')

# Создаем список размером n
n = int(str)
list = []
for i in range(n):
    list.append(i)

# Перемешиваем список
from random import randint
def list_random(value):
    result = []
    index_read = []
    index_write = 0
    while index_write < len(value):
        x = randint(0,len(list)-1)
        if x not in index_read:
            result.append(value[x])
            index_write += 1
            index_read.append(x)

    return result

# Перемешиваем список
# def list_random(value): 
#     list = []
#     for i in range(len(value)):
#         if i%2 == 0:
#             list.append(value[i])
#         else:
#             list.insert(0,value[i])
    
#     return list


print(f'Исходный список     -> {list}')
print(f'Перемешанный список -> {list_random(list)}')

