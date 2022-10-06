# Задача 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.    
# in -> 54  
# out -> [2, 3, 3, 3]  
# in -> 9990  
# out -> [2, 3, 3, 3, 5, 37]  
# in -> 650  
# out -> [2, 5, 5, 13]  

input_string = input('Введите число: ')
while not input_string.isdigit():
    print('Ошибка ввода.')
    input_string = input('Введите число: ')
input_number = int(input_string)

mul_list = []
divider = 2
while input_number/divider != 1:
    if not input_number%divider:
        input_number /= divider
        mul_list.append(divider)
    else:
        divider += 1
else:
    mul_list.append(divider)

print(f'Простые множители числа: {mul_list}')