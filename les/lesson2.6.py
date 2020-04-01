goods = int(input("Введите количество товара: "))

my_dict = []
my_list = []
n = 1

while n <= goods:
    my_dict = dict({'название': input("Введите название: "), 'цена': input("Введите цену: "),
                    'количество': input('Введите количество: '), 'eд': input("Введите единицу измерения: ")})
    my_list.append((n, my_dict))
    n += 1

print(my_list)
