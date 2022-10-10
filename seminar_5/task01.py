# Задача №1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Заполняем тестовый файл записями 
with open("task01.txt", "w") as file:
    file.write('Снежинка, дом, забвение, зимбабве, яблоня, дуб, береза' + '\n')
    file.write('Незабвенный, урок, забвение, самозабвенность, кактус, кот.'+ '\n')
    
# читаем все строки и удаляем переводы строк
with open("task01.txt", "r") as file_read:
    lines_poly = file_read.readlines()
    lines_poly = [line.rstrip('\n') for line in lines_poly]


# Процедура удаления слов
def del_word(value_str: str, value_char: str):
    print(f'in  -> {value_str}')
    del_list = [i for i in value_str.split() if i.find(value_char)>=0]

    for i in range(len(del_list)):
        value_str = value_str.replace(del_list[i], '', 1)
    value_str = value_str.replace('   ', ' ').replace('  ', ' ')
    print(f'out -> {value_str}')
    return value_str

# Программа удаления слов содержащих "абв" и записи в файл
with open('del_word_task01.txt', 'w') as file_result:
         file_result.write('')
         
for i in range(len(lines_poly)):
    clear_string = del_word(lines_poly[i], 'абв')

    with open('del_word_task01.txt', 'a') as file_result:
         file_result.write(clear_string + '\n')