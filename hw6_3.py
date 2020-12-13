'''Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
 быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
 например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
 на базе класса Worker. В классе Position реализовать методы получения полного
  имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
  Проверить работу примера на реальных данных (создать экземпляры класса Position,
   передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''



class Worker:
    name = []
    surname = []
    position = []
    _income = {'wage': 5, 'bonus': 5}
    _income_all = []
    count = 0
    def __init__(self):
        self.name.append(input(f'Введите имя:'))
        self.surname.append(input(f'Введите Фамилию:'))
        self.position.append(input(f'Введите Должность:'))
        self._income['wage'],self._income['bonus'] =input(f'Введите оклад:'),input(f'Введите премию:')
        self._income_all.append(self._income)
        self.count +=1



class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name[0]} {self.surname[0]}')
    def get_total_income(self):
        print(f'Доход  сотрудника: {int(self._income.get("wage")) + int(self._income.get("bonus"))} руб.')



worker = Position()
worker.get_full_name()
worker.get_total_income()
print(worker.name)
print(worker.surname)
print(worker._income)
print(worker._income_all)

