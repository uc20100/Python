# Задача 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Без использования: встроенной функции преобразования строк.
# in >> 13
# out >> 1101
# in >> 88
# out >> 1011000


def decimal_to_binary (value):
    BASE_NUMBER_CONVERT = 2
    BASE_NUMBER_OUT = 10

    count = 0
    result_out = 0
    while value//BASE_NUMBER_CONVERT > 0:
        result_out += (value%BASE_NUMBER_CONVERT)*BASE_NUMBER_OUT**(count)
        value //= BASE_NUMBER_CONVERT
        count += 1
    else:
        result_out += value * BASE_NUMBER_OUT**(count)
        return result_out 


string_input = input('Введите десятичное число: ')
while string_input.isdigit() == False:
    print('Ошибка ввода.')
    string_input = input('Введите десятичное число: ')
dec_number = int(string_input)

print(f'Dec: {dec_number}, Bin: {decimal_to_binary(dec_number)}')

