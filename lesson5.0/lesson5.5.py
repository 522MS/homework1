from functools import reduce


def my_func(prev_el, el):
    return prev_el + el


list = []
with open("les5.txt", "w+") as f:
    f.writelines(input('Введите числа через пробел: '))
    if f.tell() != 0:
        f.seek(0)
    lines = f.readlines()

    for i in lines:
        i = i.split()
        for j in i:
            list.append(int(j))
    print(f'Сумма чисел равна - {reduce(my_func, list)}')
