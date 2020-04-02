def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a >= b and c >= b:
        return a + c
    else:
        return b + c


print(my_func(int(input('Введите число a: ')), int(input('Введите число b: ')), int(input('Введите число c: '))))
