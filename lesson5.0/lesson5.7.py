import json

salary = []
list = []
with open('les7.txt') as f:
    lines = f.readlines()
    x = 0
    for i in lines:
        i = i.split()

        profit = int(i[2]) - int(i[3])
        print(f'Прибыль {i[0]} = {profit}')
        if profit > 0:
            salary.append(profit)
        list.append({i[0]: profit})
    print(f'Средняя прибыль = {sum(salary)}')
    list.append({'profit': profit})

print(list)

with open('Helen.json', 'w') as fj:
    json.dump(list, fj)
