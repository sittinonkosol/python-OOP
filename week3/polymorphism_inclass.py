class Employee:
    def __init__(self, name, salary, department):
        self._name = name
        self.__salary = salary
        self.__department = department
    
    def work(self):
        return f'{self._name} is working'
    
    @property
    def name(self):
        return self._name
    
class Programer(Employee):
    def work(self):
        return f'{self._name} is Programer'
    
class Accounting(Employee):
    def work(self):
        return f'{self._name} is Accounting'
    
class Sale(Employee):
    def work(self):
        return f'{self._name} is Sale'

emp1 = Programer('Non', 90000, 'ICT')
emp2 = Accounting('Jane', 100000, 'Finance')
emp2 = Accounting('Chaba', 50000, 'Marketing')