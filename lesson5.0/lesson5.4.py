translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
list = []

with open('les4.txt') as f:
    lines = f.readlines()
    for i in lines:
        i = i.split()
        list.append(f'{translate[i[0]]} {i[1]} {i[2]}\n')

with open ('les4_new.txt', 'w+') as f_new:
    f_new.writelines(list)


