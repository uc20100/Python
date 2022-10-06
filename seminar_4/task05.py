# Задача 5. Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.   
# poly.txt     -> 3*x^9 + 3*x^8 - 2 = 0
# poly_2.txt   -> 3 + 2*x^2 + 2*x^1 = 0
# poly + poly_2 = 3*x^9 + 3*x^8 + 2*x^2 + 2*x^1 + 1 = 0 

# процедура сложения многочленов
def sum_polynomial(value_1: str, value_2: str):
    NO_VALUE = ''
    result_list = []
    result_out = ''
    value_1 = value_1.replace('+','$+').replace('-','$-').replace('=','$=$').replace(' ', '')
    value_2 = value_2.replace('+','$+').replace('-','$-').replace('=','$=$').replace(' ', '')
    polynomial_string = (f'{value_1}${value_2}')
    polynomial_list = polynomial_string.split('$')
    number_value = 0
    for i in range(len(polynomial_list)):
        if polynomial_list[i].find('^')>0:
            find_value_list = polynomial_list[i].split("*")
            type_polynomial = find_value_list[1]
            ratio_polynomial = 0
            for j in range(i,len(polynomial_list)):
                if polynomial_list[j].find(type_polynomial)>0:
                    temp_list = polynomial_list[j].split('*')
                    ratio_polynomial += int(temp_list[0])
                    polynomial_list[j] = NO_VALUE
            result_list.append(f'{ratio_polynomial}*{type_polynomial}')    
        else:
            if polynomial_list[i].find('=')<0 and polynomial_list[i] != NO_VALUE:
                if polynomial_list[i-1] == '=' or (polynomial_list[i-2] == '=' and polynomial_list[i-1] == ''):
                    number_value -= int(polynomial_list[i])
                else:
                    number_value += int(polynomial_list[i])

    result_list.append(f'{number_value}')

    for i in range(len(result_list)):
        if i == 0:
            result_out += (f'{result_list[i]}')
        else:
            if result_list[i][0] != '-':
                result_out += (f'+{result_list[i]}')
            else:
                result_out += (f'{result_list[i]}')
    
    result_out = (f'{result_out}=0')
    result_out = result_out.replace('+',' + ').replace('-',' - ').replace('=',' = ')
    return result_out
     

# Заполняем файл записями 
with open("poly.txt", "w") as file:
    file.write('3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0' + '\n')
    file.write('-3*x^2 - 10 + 3*x^2 + 1*x^1 = 2' + '\n')
    file.write('3*x^9 + 3*x^8 - 2 = 0' + '\n')

# Заполняем файл записями 
with open("poly_2.txt", "w") as file:
    file.write('3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 25 = 0' + '\n')   
    file.write('3*x^9 + 3*x^8 + 2 = -1' + '\n')
    file.write('3 + 2*x^2 + 2*x^1 = 0' + '\n')


# читаем все строки и удаляем переводы строк
with open("poly.txt", "r") as file_poly:
    lines_poly = file_poly.readlines()
    lines_poly = [line.rstrip('\n') for line in lines_poly]
    
# читаем все строки и удаляем переводы строк
with open("poly_2.txt", "r") as file_poly_2:
    lines_poly_2 = file_poly_2.readlines()
    lines_poly_2 = [line.rstrip('\n') for line in lines_poly_2]

# записываем сумму многочленов в файл и выводим её на экран 
with open('sum_poly.txt', 'w') as file:
    for i in range(min(len(lines_poly), len(lines_poly_2))):
        print(f'poly.txt      -> {lines_poly[i]}')
        print(f'poly_2.txt    -> {lines_poly_2[i]}')
        sum_poly = sum_polynomial(lines_poly[i], lines_poly_2[i])
        print(f'poly + poly_2 -> {sum_poly}')
        print('')
        file.write(sum_poly + '\n')

