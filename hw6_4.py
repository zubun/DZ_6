'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
 speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
  которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите
  несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
  класс метод show_speed, который должен показывать текущую скорость автомобиля. Для
  классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше
  60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
'''


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        self.info()

    def info(self):
        print(f'Марка автомобиля: {self.name}')
        print(f'Цвет автомобиля: {self.color}')
        # print(f'Скорость автомобиля:{self.speed}')
        self.show_speed()
        if self.is_police == True:
            print('Вы Передвигаетесь на полицейской машине')
        print('______________________')

    def go(self):
        print(f'Машина поехала!')
        print('______________________')

    def stop(self):
        print(f'Машина остановилась!')
        print('______________________')

    def turn(self):
        print(f'Машина повернула!')
        print('______________________')
    def show_speed(self):
        print(f'Текущая скорость: {self.speed} км/ч.')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили скорость на: {self.speed - 60} км/ч.')
        else:
            print(f'Текущая скорость: {self.speed} км/ч.')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили скорость на: {self.speed - 40} км/ч.')
        else:
            print(f'Текущая скорость: {self.speed} км/ч.')
class PoliceCar(Car):
    pass



car_one = Car('BMW', 'Green', 150, False)

car_two = TownCar('Lexus', 'Black', 70, False)

car_three = SportCar('Ferrari', 'Red', 300, False)

car_for = WorkCar('WV', 'Blue', 100, False)

car_five = PoliceCar('Shkoda', 'Pink', 100, True)

car_one.go()
car_two.stop()
car_for.turn()


