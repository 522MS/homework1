class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        return self.quantity - other.quantity if self.quantity > other.quantity else 'Колличесво ячеек отрицательное!!!'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, cells_in_a_row):
        my_str = []
        for i in range(self.quantity):
            my_str.append('*') if (i + 1) % cells_in_a_row != 0 else my_str.append('*\\n')
        print(''.join(my_str))


c1 = Cell(14)
c2 = Cell(3)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
c1.make_order(3)
