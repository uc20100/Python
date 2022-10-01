#  Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.     
# in >> 8  
# out >> -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21  
# in >> 3  
# out >> 2 -1 1 0 1 1 2

def fibonacci_list (value):
    result = [i for i in range(-value, value+1)]
    result[result.index(0)-1] = 1
    for i in range(result.index(0)+2, len(result), 1):
        result[i] = result[i-1] + result[i-2]
    for i in range(result.index(0)-2, -1, -1):
        result[i] = result[i+2] - result[i+1]    
    return result 



console_string = input('Введите число: ')
while console_string.isdigit() == False:
    print('Введённые символы не являются натуральным числом')
    console_string = input('Введите число: ')

print(fibonacci_list(int(console_string)))

