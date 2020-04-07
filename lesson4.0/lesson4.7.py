from math import factorial

def fact(n):
    yield factorial(n)


n = int(input('Введите число: '))
for el in fact(n):
    print(f'Факториал числа {n} равен {el}')
