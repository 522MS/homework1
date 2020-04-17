from abc import ABC, abstractmethod


class MyAbstractClass(ABC):

    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def costume(self):
        pass


class Garment(MyAbstractClass):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def coat(self):
        return self.v / 6.5 + 0.5

    @property
    def costume(self):
        return 2 * self.h + 0.3

    def summ_garment(self):
        print(f'Общий расход ткани равен - {self.coat + self.costume}')


g = Garment(150, 200)
print(g.coat)
print(g.costume)
g.summ_garment()
