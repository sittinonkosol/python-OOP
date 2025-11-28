class Employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        self.__emp_id = emp_id
        self.__name = emp_name
        self._base_salary = emp_salary

    @property
    def emp_id(self):
        return self.__emp_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value):
        if value > 0:
            self._base_salary = value
    
    def calculate_salary(self):
        return {'base_salary' : self.base_salary, 'calculated_salary' : self.base_salary / 12}
    
    def __str__(self):
        return f'Employee(emp_id={self.emp_id}, name={self.name}, base_salary={self.calculate_salary()})'

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, emp_name, emp_salary, emp_bonus_rate):
        super().__init__(emp_id, emp_name, emp_salary)
        self._bonus_rate = float(emp_bonus_rate)

    def calculate_salary(self):
        total_salary = self.base_salary + (self.base_salary * self._bonus_rate)
        return total_salary

    def __str__(self):
        return f'Employee(emp_id = {self.emp_id}, emp_name = {self.name}, emp_salary = {self.base_salary}, emp_bonus_rate = {self._bonus_rate}), total_salary = {self.calculate_salary()}'

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours):
        super().__init__(emp_id, name, hourly_rate)
        self._work_hour = hours

    def calculate_salary(self):
        total_salary = self._work_hour * self.base_salary
        return total_salary

    def __str__(self):
        return f'Employee(emp_id = {self.emp_id}, emp_name = {self.name}, emp_salary = {self.base_salary}, work_hour = {self._work_hour}), total_salary = {self.calculate_salary()}'


if __name__ == "__main__":
    emp1 = FullTimeEmployee("E001", "Ann", 30000, 0.1)
    emp2 = FullTimeEmployee("E002", "Bob", 35000, 0.1)
    emp3 = PartTimeEmployee("E003", "Cindy", 100, 120)
    
    employees = [emp1, emp2, emp3]
    for emp in employees:
        print(emp)
        print(f"{emp.emp_id} {emp.name} salary = {emp.calculate_salary()}")
        print("-" * 40)
