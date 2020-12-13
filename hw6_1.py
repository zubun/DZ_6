'''Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный. В рамках метода
реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый)
— 2 секунды, третьего (зеленый) — на ваше усмотрение.  Переключение между режимами
должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.'''



# class Auto:
#     # атрибуты класса
#     auto_count = 0
#
#     # методы класса
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         print("Автомобиль заведен")
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count += 1
#
# a = Auto()
# a.on_auto_start("Lexus", "RX 350L", 2019)
# print(a.auto_name)
# print(a.auto_count)

class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def ranning(self):
        count = 0
        while count < 5:
            for el in self.__color:
                print(f'Горит {el}')
                if el == 'red':
                    for i in reversed(range(1, 8)):
                        print(i)
                        continue
                if el == 'yellow':
                    for i in reversed(range(1, 3)):
                        print(i)
                        continue
                if el == 'green':
                    for i in reversed(range(1, 6)):
                        print(i)
                        continue
            count += 1



a = TrafficLight()
a.ranning()

