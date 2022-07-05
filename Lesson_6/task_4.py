class Car:
    "Автомобиль"

    def __init__(self, name, color, is_police=False):
        self.name = name
        self.color = color
        self.speed = None
        print(f'New car: {self.name} (color: {self.color}), Police car : {is_police}')

    def go(self, speed):
        self.speed = speed
        print(f'{self.name}: The car is moving')

    def stop(self):
        self.speed = 0
        print(f'{self.name}: The car stopped')

    def turn(self, direction):
        print(f'{self.name}: The car turned {"left" if direction == 0 else "right"}')

    def show_speed(self):
        return f'{self.name}: travelling speed {self.speed}'


class TownCar(Car):
    "Городской автомобиль"

    def show_speed(self):
        return f'{self.name}: travelling speed {self.speed}. Overspeed.' \
            if self.speed > 60 else f'{self.name}: travelling speed {self.speed}'


class WorkCar(Car):
    "Рабочая машина"

    def show_speed(self):
        return f'{self.name}: travelling speed {self.speed}. Overspeed.' \
            if self.speed > 40 else f'{self.name}: travelling speed {self.speed}'


class SportCar(Car):
    "Спортивная машина"


class PoliceCar(Car):
    "Полицейская машина"
    is_police = True


work_car = WorkCar('MAN', 'Black')
work_car.go(47)
work_car.turn(0)
print(work_car.show_speed())

print()
town_car = TownCar('BMW', 'Blue')
town_car.go(55)
town_car.stop()
print(town_car.show_speed())
print()

police_car = PoliceCar('Volvo', 'Black', True)
police_car.go(300)
police_car.turn(1)
print(police_car.show_speed())

print(f'\nCar {police_car.name} - color: {police_car.color}')
print(f'Car {work_car.name} - color: {work_car.color}')

