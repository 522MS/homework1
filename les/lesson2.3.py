month_number = int(input('Введите месяц в виде числа: '))

mounth = {1: 'Январь',
          2: 'Февраль',
          3: 'Март',
          4: 'Апрель',
          5: 'Май',
          6: 'Июнь',
          7: 'Июль',
          8: 'Август',
          9: 'Сентябрь',
          10: 'Октябрь',
          11: 'Ноябрь',
          12: 'Декабрь'}

season = ['зимма', 'весна', 'лето', 'осень']


if month_number == 12 or month_number == 1 or month_number == 2:
   print(f'месяц {mounth[month_number]} относится к времени года {season[0]}')
elif month_number == 3 or month_number == 4 or month_number == 5:
    print(f'месяц {mounth[month_number]} относится к времени года {season[1]}')
elif month_number == 6 or month_number == 7 or month_number == 8:
    print(f'месяц {mounth[month_number]} относится к времени года {season[2]}')
elif month_number == 9 or month_number == 10 or month_number == 11:
    print(f'месяц {mounth[month_number]} относится к времени года {season[3]}')

