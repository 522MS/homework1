file = open('les2.txt')

lines = file.readlines()

x = 0
for i in lines:
    x += 1
print(f'Колличество строк - {x}')

y = 0
for i in lines:
    words = lines[y].count(' ')
    print(f'В строке №{y + 1} - {words + 1} слова')
    y += 1