# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

str = input('Введите число: ')
while str.isdigit() == False:
    print('Введённые символы не являются натуральным числом')
    str = input('Введите число: ')

n = int(str)
list = []
for i in range(n):
    if i == 0:
        list.append(i+1)
    else:
        list.append((i+1)*list[i-1])

print('-> ', list)

