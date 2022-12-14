# ДЗ по "Знакомство с языком программирования Python"
## Семинар 1
- Задача 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.  
Пример:  
6 -> да  
7 -> да  
1 -> нет  

- Задача 7. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  

- Задача 8. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).  
Пример:  
x=34; y=-30 -> 4  
x=2; y=4-> 1  
x=-34; y=-30 -> 3  

- Задача 9. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).  

- Задача 10. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.  
Пример:  
A (3,6); B (2,1) -> 5,09  
A (7,-5); B (1,-1) -> 7,21  


## Семинар 2
- Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.  
Пример:  
6782 -> 23  
0,56 -> 11  

- Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.  
Пример:  
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)  
  

- Задача 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.  
Пример:  
Для n = 6: {2, 2, 2, 2, 2, 3} -> 13  

- Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].  
Найдите произведение элементов на указанных позициях (не индексах). Позиции хранятся в файле file.txt в одной строке одно число.  
Position one: 1  
position two: 3  
Number of elements: 5  
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] -> 15  
 
- Задача 5. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random  
 -> 10  
 -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
 -> [0, 7, 6, 1, 4, 2, 8, 3, 5, 9]  

 ## Семинар 3

- Задача 1. Задайте список, состоящий из произвольных чисел, количество задает пользователь. Напишите программу, которая найдет сумму элементов списка, стоящих на нечетных позициях (не индексах).  
in -> 4  
out -> [7, 9, 2, 3]  
out -> 9  
in -> 5  
out -> [2, 5, 2, 7, 9]  
out -> 13   

- Задача 2. Напишите программу, которая найдет произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.  
in -> 4  
out -> [8, 9, 10, 10]  
out -> [80, 90]  
in -> 5  
out -> [3, 3, 6, 8, 4]  
out -> [12, 24, 6]  

- Задача 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без использования: встроенной функции преобразования строк.  
in -> 13  
out -> 1101  
in -> 88  
out -> 1011000  

- Задача 4. Задайте список из произвольных вещественных чисел, количество задает пользователь. Напишите программу, которая найдет разницу между максимальным и минимальным значением дробной части элементов.  
in -> 3  
out -> [2.84, 9.42, 1.87]  
out -> "Min: 0.42, Max: 0.87, Difference: 0.45  
 
- Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.   
in -> 8  
out -> -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21  
in -> 3  
out -> 2 -1 1 0 1 1 2   

## Семинар 4

- Задача 1. Вычислить число с заданной точностью d.  
in -> Enter a real number: 9  
in -> Enter the required accuracy '0.0001': 0.000001  
out -> 9.000000  
in -> Enter a real number: 8.98765  
in -> Enter the required accuracy '0.0001': 0.001    
out -> 8.988   

- Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.    
in -> 54  
out -> [2, 3, 3, 3]  
in -> 9990  
out -> [2, 3, 3, 3, 5, 37]  
in -> 650  
out -> [2, 5, 5, 13]  

- Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов последовательности в том же порядке.  
in -> 10  
out -> [4, 4, 5, 5, 6, 2, 3, 8, 9, 4]  
out -> [6, 2, 3, 8, 9]  

- Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.  
 
- Задача 5. Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.   
poly.txt      -> 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0  
poly_2.txt    -> 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 25 = 0  
poly + poly_2 -> 6*x^9 + 6*x^8 - 4*x^6 + 2*x^5 - 6*x^4 - 2*x^2 + 4*x^1 + 33 = 0  
poly.txt      -> -3*x^2 - 10 + 3*x^2 + 1*x^1 = 2  
poly_2.txt    -> 3*x^9 + 3*x^8 + 2 = -1  
poly + poly_2 -> 0*x^2 + 1*x^1 + 3*x^9 + 3*x^8 - 9 = 0  

## Семинар 5

- Задача 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".   

- Задача 2. Создайте программу для игры с конфетами человек против человека. 
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?  
a) Добавьте игру против бота  
b) Подумайте как наделить бота "интеллектом"   

- Задача 3. Создайте программу для игры в "Крестики-нолики".  

- Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.  

- Входные и выходные данные хранятся в отдельных текстовых файлах.  

## Семинар 6

- Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение  
Формат: Объясняет преподаватель  

- Задача: предложить улучшения кода для уже решённых задач:  
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension 
В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.  

## Семинар 7

- **Задание в группах:** Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.  
*под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, пустая строка - разделитель*
    
  
    *Фамилия_1*  
    *Имя_1*  
    *Телефон_1*  
    *Описание_1*  

    *Фамилия_2*  
    *Имя_2*  
    *Телефон_2*  
    *Описание_2*  
    *и т.д.в файле на одной строке хранится все записи, символ разделитель - ';'* 
        
    *Фамилия_1,Имя_1,Телефон_1,Описание_1*  
    *Фамилия_2,Имя_2,Телефон_2,Описание_2*  

## Семинар 8

- Доделать решение задачи: Задача: Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы   

## Семинар 9

- Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP( можно любую задачу, главное файл с библиотекой чтобы был в формате тхт).  
- Прикрутить бота к задачам с предыдущего семинара:  
Создать калькулятор( можно добавить работу с рациональными и комплексными числами), организовать меню, добавив в неё систему логирования   

## Семинар 10  

- Прикрутить бота к задачам с предыдущего семинара:  
Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования  

## Семинар 11  

- https://colab.research.google.com/drive/11udiVDM85HFjqLqDqfz0ef9NLBgHUWn-?usp=sharing  
по ссылке скопировать себе этот файл и выполнить все задания (3 модуля заданий). делать лучше в гугл коллаб, но если удобней в другой среде, то можно и в них. Задания с помощью Pandas  
