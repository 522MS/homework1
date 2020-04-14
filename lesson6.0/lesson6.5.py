class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Ручка - {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш - {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Маркер - {self.title}')


s = Stationery('')
s.draw()
p = Pen('шириковая')
p.draw()
pc = Pencil('простой')
pc.draw()
h = Handle('не смывающийся')
h.draw()
