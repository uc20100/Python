# Задача 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# Пример:
# - Для n = 6: {2, 2, 2, 2, 2, 3} -> 13

str = input('Введите число: ')
while str.isdigit() == False:
    print('Введённые символы не являются натуральным числом')
    str = input('Введите число: ')

n = int(str)
list = []

for i in range(1,n+1,1):
    list.append(round((1+1/i)**i))

sum = 0    
for i in list:
    sum += i

print(f'{list} -> {sum}')