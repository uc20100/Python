# Задача 1. Вычислить число с заданной точностью d.  
# in -> Enter a real number: 9  
# in -> Enter the required accuracy '0.0001': 0.000001  
# out -> 9.000000  
# in -> Enter a real number: 8.98765  
# in -> Enter the required accuracy '0.0001': 0.001    
# out -> 8.988   



def test_float (value):
    result_out = True
    try:
        f = float(value)    
    except Exception as e:
        print(e)
        result_out = False
    return result_out

def test_format_float (value):
    result_out = False
    if test_float(value):
       if float(value) == 1/10**(len(value)-2) or float(value) == 0:
            result_out = True
    return result_out



string_number = input('Enter a real number: ')
while not test_float(string_number):
    string_number = input('Enter a real number: ')

string_accuracy = input('Enter the required accuracy \'0.0001\': ')
while not test_format_float(string_accuracy) :
    print('Error format')
    string_accuracy = input('Enter the required accuracy \'0.0001\': ')

if not float(string_accuracy):
    position_accuracy = 0
else:
    position_accuracy = len(string_accuracy)-2

print(f'result -> {float(string_number):.{position_accuracy}f}')


