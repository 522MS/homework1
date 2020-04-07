from itertools import count, cycle

for number in count(3):
    print(number)
    if number > 9:
        break

my_list = ['name', 'surname', 'age']
x = 0
for i in cycle(my_list):
    print(i)
    x += 1
    if x > 9:
        break
