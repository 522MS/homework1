from time import sleep


class TrafficLight:
    _color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        for i in range(3):
            print(a._color[0])
            sleep(7)
            print(a._color[1])
            sleep(2)
            print(a._color[2])
            sleep(5)


a = TrafficLight()
a.running()
