# Задача №1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

input_string = 'Снежинка, дом, забвение, зимбабве, яблоня, дуб, береза, ' + \
               'незабвенный, урок, забвение, самозабвенность, кактус, кот.'

print(f'in  -> {input_string}')
del_list = [i for i in input_string.split() if i.find('абв')>0]

for i in range(len(del_list)):
    input_string = input_string.replace(del_list[i], '', 1)
input_string = input_string.replace('   ', ' ').replace('  ', ' ')
print(f'out -> {input_string}')