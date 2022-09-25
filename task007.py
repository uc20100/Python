# Задача №7
# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.



def test_bool(x, y, z):
    max_len = max(len(f'{x:0b}'),len(f'{y:0b}'),len(f'{z:0b}'))
    mask = 2**max_len-1
    value1 = ~(x|y|z) & mask
    print(f'¬(x ⋁ y ⋁ z) -> ¬({x:0{max_len}b} ⋁ {y:0{max_len}b} ⋁ {z:0{max_len}b}) = {value1:0{max_len}b}')
    value2 = ~x & ~y & ~z & mask
    print(f'¬(x) ⋀ ¬(y) ⋀ ¬(z) -> {(~x&mask):0{max_len}b} ⋀ {(~y&mask):0{max_len}b} ⋀ {(~z&mask):0{max_len}b} = {value2:0{max_len}b}')
    return value1==value2


x = int(input('Введите значение "х": ')) # 8 dec -> 0000 1000 bin
y = int(input('Введите значение "y": ')) # 240 dec -> 1111 0000 bin
z = int(input('Введите значение "z": ')) # 4 dec -> 0000 0100 bin
print('')
if test_bool(x,y,z):
    print('Утверждение истинно')
else:
    print('Утверждение ложно')

 