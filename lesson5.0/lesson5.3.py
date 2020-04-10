with open('les3.txt') as f:
    salary = []
    lines = f.readlines()
    x = 0
    for i in lines:
        i = i.split()
        if int(i[1]) < 20000:
            print(f'Оклад сотрудника {i[0]} - меньше 20000')
        salary.append(int(i[1]))
        x += 1
    print(f'Средняя велечина дохода сотрудников = {sum(salary) / x}')
