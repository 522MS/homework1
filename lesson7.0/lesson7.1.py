class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join('\t'.join(map(str, i)) for i in self.my_list)

    def __add__(self, other):
        self.my_list.append(other)


m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
a = []
b = []
m_sum = Matrix([a, b])
print(m1, '\n')
print(m2, '\n')
for i in range(2):
    a.append(m1.my_list[0][i] + m2.my_list[0][i])
    m1 + a
for i in range(2):
    b.append(m1.my_list[1][i] + m2.my_list[1][i])
    m1 + b
print(m_sum)