class Worker:
    name = 'Иван'
    surname = 'Иванов'
    position = 'Бухгалтер'
    _income = {"wage": 20000, "bonus": 5000}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        income = self._income["wage"] + self._income["bonus"]
        print(f'Доход сотрудника с учетом препии - {income}')



a = Position()
print(a.position)
a.get_full_name()
a.get_total_income()
