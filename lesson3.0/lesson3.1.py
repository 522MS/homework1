def division(a, b):
    return a / b
try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    print(division(a, b))
except ZeroDivisionError:
    print('Делить на 0 нельзя')


