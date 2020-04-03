sum_res = 0
a = True
while a:
    x = 0
    print('Для завершения нажмите q')
    numbers = list(input('Введите числа для сложения: ').split())

    for i in range(len(numbers)):
        if 'q' == numbers[i]:
            a = False
            break
        x = x + int(numbers[i])

    sum_res = sum_res + x
    print(sum_res)