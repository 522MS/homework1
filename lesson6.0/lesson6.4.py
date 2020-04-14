class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        if direction == 'right':
            print(f'Автомобиль {self.name} повернул вправо')
        elif direction == 'left':
            print(f'Автомобиль {self.name} повернул  влево')

    def show_speed(self):
        print(f'Текущая скорость авто {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость авто {self.speed}')
        if self.speed > 60:
            print('Скорость превышена!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость авто {self.speed}')
        if self.speed > 40:
            print('Скорость превышена!')


class PoliceCar(Car):
    def police(self):
        if self.is_police == True:
            print(f'{self.name} - полицейская машина')


tc = TownCar(100, 'yellow', 'Mercedes', False)
tc.go()
tc.show_speed()
tc.turn('right')
tc.turn('left')
tc.stop()

sc = SportCar(120, 'blue', 'Ferrari', False)
sc.go()
sc.turn('right')
sc.stop()

wc = WorkCar(60, 'black', 'Hyundai', False)
wc.show_speed()
pc = PoliceCar(80, 'white', 'Lada', True)
pc.go()
pc.stop()
pc.police()