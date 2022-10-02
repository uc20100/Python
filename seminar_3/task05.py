#  Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.     
# in >> 8  
# out >> -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21  
# in >> 3  
# out >> 2 -1 1 0 1 1 2

def fibonacci_list (value):
    result_out = [i for i in range(-value, value+1)]
    result_out[result_out.index(0)-1] = 1
    for i in range(result_out.index(0)+2, len(result_out), 1):
        result_out[i] = result_out[i-1] + result_out[i-2]
    for i in range(result_out.index(0)-2, -1, -1):
        result_out[i] = result_out[i+2] - result_out[i+1]    
    return result_out 



console_string = input('Введите число: ')
while console_string.isdigit() == False:
    print('Введённые символы не являются натуральным числом')
    console_string = input('Введите число: ')

print(f'Список Фибоначчи: {fibonacci_list(int(console_string))}')

