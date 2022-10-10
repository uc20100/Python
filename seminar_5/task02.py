# Задача №2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

MIN_GET_CANDY = 1
MAX_GET_CANDY = 28
ALL_CANDY = 2021

# Процедура взятия конфет
def get_candy(gamer_name: str, candy_size, old_user_candy, fist_gamer_name):  
    if gamer_name.find('BOT_') >= 0:    
        if gamer_name == fist_gamer_name: 
            if candy_size == ALL_CANDY:
                return_candy = ALL_CANDY - ((MIN_GET_CANDY+MAX_GET_CANDY)*(ALL_CANDY//(MIN_GET_CANDY+MAX_GET_CANDY)))
            else:
                return_candy = MAX_GET_CANDY + MIN_GET_CANDY - old_user_candy       
        else:
            if candy_size <= MAX_GET_CANDY:
                return_candy = candy_size
            else:
                return_candy = random.randint(MIN_GET_CANDY, MAX_GET_CANDY)  
        print(f'{gamer_name}, взял {return_candy} конфет ')
        return return_candy
    else:       
        in_string = input(f'{gamer_name}, возьмите конфеты от {MIN_GET_CANDY} до {MAX_GET_CANDY}: ')
        try:
            n_candy = int(in_string)    
        except Exception as e:
            # print(e)
            return 0
        if MIN_GET_CANDY<=n_candy<=MAX_GET_CANDY and n_candy<=candy_size:
            return n_candy
        else:
            return 0

print('Игра может происходить между двумя людьми или между человеком и ботом или между двумя ботами')
print('Чтобы сыграть с ботом задайте имя игрока BOT_1, чтобы посмотреть как играют два бота задайте имена игроков BOT_1 и BOT_2')
user_1_name = input('Введите имя игрока 1: ')
user_2_name = input('Введите имя игрока 2: ')

import os
import random
if 0<random.randint(1,100)<50:
    name_gamer_first = user_1_name
    name_gamer_second = user_2_name
else:
    name_gamer_first = user_2_name
    name_gamer_second = user_1_name
print(f'Брошен жребий, первым будет ходить {name_gamer_first}, вторым {name_gamer_second}')
trigger_user = 1
first_gamer_candy = 0
second_gamer_candy = 0
last_gamer_candy = 0
residue_candy = ALL_CANDY
leader = 'Non'

# Программа игры
while residue_candy>0:
    if trigger_user == 1:
        user = name_gamer_first
    else:
        user = name_gamer_second
    print (f'Всего конфет: {residue_candy}  Первый игрок {name_gamer_first}: {first_gamer_candy}   Второй игрок {name_gamer_second}: {second_gamer_candy}')
    while residue_candy>0:
        get_gamer_candy = get_candy(user,residue_candy,last_gamer_candy,name_gamer_first)
        if get_gamer_candy > 0:
            if trigger_user == 1:
                first_gamer_candy += get_gamer_candy
            else:
                second_gamer_candy += get_gamer_candy
            residue_candy -= get_gamer_candy
            if residue_candy == 0:
                leader = user
            break
        print('Ошибка, повторите ввод')
    last_gamer_candy = get_gamer_candy
    if trigger_user == 1:
        trigger_user = 2
    else:
        trigger_user = 1
    # os.system('cls') 
else:
    print(f'Победил {leader} !!!')


