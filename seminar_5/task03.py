# Задача 3. Создайте программу для игры в ""Крестики-нолики"".

# поле крестиков ноликовФ
field = [[' ','1','2','3'],['A',' ',' ',' '],['B',' ',' ',' '],['C',' ',' ',' ']]

# Проверка корректности ввода
def set_step(coordinates: str, value: str):
    if coordinates[0] == 'A':
        in_char_number = 1
    elif coordinates[0] == 'B':
        in_char_number = 2
    elif coordinates[0] == 'C':
        in_char_number = 3    
    in_number = int(coordinates[1])

    if field[in_char_number][in_number] == ' ':
        field[in_char_number][in_number] = value
        return True
    else:
        print('Так нельзя ходить')
        return False

# Ввод крестика или нолика по координатам
def in_coordinates(value: str):
    while True:
        in_string = input(f'Введите координаты куда нужно поставить {value}, (в формате A1, C3, B2): ')
        if in_string in ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'):
            if set_step(in_string, value):
                return True
        else:
            print('Ошибка формата данных')

# Печать поля крестиков ноликов
def print_field():
    for i in range(4):
        print(f'{field[i][0]} {field[i][1]} {field[i][2]} {field[i][3]}')

# Процедура проверки на окончание игры
def check (value):
    if f'{value[1][1]}{value[1][2]}{value[1][3]}' == 'XXX' or 'OOO' == f'{value[1][1]}{value[1][2]}{value[1][3]}':
        return True
    elif f'{value[2][1]}{value[2][2]}{value[2][3]}' == 'XXX' or 'OOO' == f'{value[2][1]}{value[2][2]}{value[2][3]}':
        return True
    elif f'{value[3][1]}{value[3][2]}{value[3][3]}' == 'XXX' or 'OOO' == f'{value[3][1]}{value[3][2]}{value[3][3]}':
        return True
    elif f'{value[1][1]}{value[2][1]}{value[3][1]}' == 'XXX' or 'OOO' == f'{value[1][1]}{value[2][1]}{value[3][1]}' == 'XXX':
        return True
    elif f'{value[1][2]}{value[2][2]}{value[3][2]}' == 'XXX' or 'OOO' == f'{value[1][2]}{value[2][2]}{value[3][2]}':
        return True
    elif f'{value[1][3]}{value[2][3]}{value[3][3]}' == 'XXX' or 'OOO' == f'{value[1][3]}{value[2][3]}{value[3][3]}':
        return True
    elif f'{value[1][1]}{value[2][2]}{value[3][3]}' == 'XXX' or 'OOO' == f'{value[1][1]}{value[2][2]}{value[3][3]}':
        return True
    elif f'{value[1][3]}{value[2][2]}{value[3][1]}' == 'XXX' or 'OOO' == f'{value[1][3]}{value[2][2]}{value[3][1]}':
        return True
    else:
        return False

# Игра в крестики нолики
char_value = 'O'
while True:
    if char_value == 'O':
       char_value = 'X' 
    else:
        char_value = 'O'
    print_field()
    if check(field):
        print('Игра окончена!')
        break
    in_coordinates(char_value)

    
   