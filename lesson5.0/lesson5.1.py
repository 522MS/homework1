my_list = []
a = True
while a:
    line = input("Введите данные: ")
    if line == '':
        print(my_list)
        a = False
    else:
        newline = line + '\n'
        my_list.append(newline)

with open("file.txt", "w") as f:
    f.writelines(my_list)