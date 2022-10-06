# Задача 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, 
# записать в файл полученный многочлен не менее 3-х раз. 

# процедура задания рандомных коэффициентов многочлена
import random
def random_cof_polynomial(value: str, min_rand, max_rand):
    NO_VALUE = ''
    result_list = []
    result_out = NO_VALUE
    polynomial_string = value.replace('+','$+').replace('-','$-').replace('=','$=$').replace(' ', '')
    polynomial_list = polynomial_string.split('$')
    for i in range(len(polynomial_list)):
        if polynomial_list[i].find('^')>0:
            find_value_list = polynomial_list[i].split("*")
            type_polynomial = find_value_list[1]
            result_list.append(f'{random.randint(min_rand, max_rand)}*{type_polynomial}')    
        else:
            if polynomial_list[i] != '=' and polynomial_list[i] != NO_VALUE:
                if len(polynomial_list)-1 == i:
                    result_list.append(f'{polynomial_list[i]}')
                else:
                    result_list.append(f'{random.randint(min_rand, max_rand)}')
            else:
                if polynomial_list[i] == '=':
                    result_list.append('=')

    for i in range(len(result_list)):
        if i == 0 or i>len(result_list)-3:
            result_out += (f'{result_list[i]}')
        else:
            if result_list[i][0] != '-':
                result_out += (f'+{result_list[i]}')
            else:
                result_out += (f'{result_list[i]}')
    
    result_out = (f'{result_out}')
    result_out = result_out.replace('+',' + ').replace('-',' - ').replace('=',' = ')
    return result_out

# список многочленов
polynomial_list = []
polynomial_list.append('3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0')
polynomial_list.append('6*x^9 + 6*x^8 - 4*x^6 + 2*x^5 - 6*x^4 - 2*x^2 + 4*x^1 + 33 = 0')
polynomial_list.append('-3*x^2 - 10 + 3*x^2 + 1*x^1 = 2')
polynomial_list.append('3*x^9 + 3*x^8 + 2 = -1')

with open('random_cof_poly.txt', 'w') as file:
    file.write('')

MIN_VALUE_RANDOM = 0
MAX_VALUE_RANDOM = 10
# случайным образом изменяем коэффициенты многочленов и записываем их в файл
for i in polynomial_list:
    print (f'old -> {i}')
    new_polynomial = random_cof_polynomial(i,MIN_VALUE_RANDOM,MAX_VALUE_RANDOM)
    print (f'new -> {new_polynomial}')
    print('')
    with open('random_cof_poly.txt', 'a') as file:
        file.write(new_polynomial + '\n')