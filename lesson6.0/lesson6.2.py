class Road:
    _length = int(input('Введите длину(в метрах): '))
    _width = int(input('Введите ширину(в метрах): '))

    def asphalt_mass(self):
        mass = self._length * self._width * 25 * 5
        print(f'{self._length}м*{self._width}м*25кг*5см = {mass}т')


road = Road()
road.asphalt_mass()
