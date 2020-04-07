from sys import argv

way, production, rate, premium = argv
print(argv)
salary = (int(production) * int(rate)) + int(premium)

print(f'Заработная плата сотрудника равна {salary}')

