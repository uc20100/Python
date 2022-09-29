# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях (не индексах). Позиции хранятся в файле file.txt в одной строке одно число.
# Position one: 1
# position two: 3
# Number of elements: 5
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] -> 15


str = input('Введите число: ')
while str.isdigit() == False:
    print('Введённые символы не являются натуральным числом')
    str = input('Введите число: ')

# Создаем список от -n до n
n = int(str)
list = []
for i in range(-n, n+1):
    list.append(i)

print(f'Список от {-n} до {n} -> {list}')

# Заполняем файл записями 
file = open("index.txt", "w")
file.write('tfglk' + '\n')
file.write('-100' + '\n')
file.write('1' + '\n')
file.write('200' + '\n')
file.write('3' + '\n')
file.close()

file = open("index.txt", "r")
# читаем все строки и удаляем переводы строк
lines = file.readlines()
lines = [line.rstrip('\n') for line in lines]
file.close()

# отфильтровываем не положительные натуральные значения и значения больше длины списка,
# подсчитываем произведение элементов на указанных позициях
product = 1
position = []
for i in lines:
    if i.isdigit() == True:
        if int(i) < len(list) and int(i)>0:
            product *= list[int(i)-1]
            position.append(i)

print(f'Произведение элементов с позициями {position} = {product}')




