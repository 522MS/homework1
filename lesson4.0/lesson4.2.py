my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [el for num, el in enumerate(my_list) if my_list[num] > my_list[num - 1] and my_list[num] != my_list[0]]

print(result)

