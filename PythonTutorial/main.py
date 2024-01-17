class Employee:
    
    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def ser_raise_amt(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    def __repr__(self) -> str:
        return "Employee('{}', '{}', '{})".format(self.first, self.last, self.pay)
    
    def __str__(self) -> str:
        return '{} - {}'.format(self.fullname(), self.email)

emp_1 = Employee('Corey','Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

Employee.ser_raise_amt(1.05)

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(emp_1.__dict__)
# print(Employee.__dict__)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'

new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 8, 10)
# print(Employee.is_workday(my_date))

print(repr(new_emp_1))

class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.prolang = pro_lang

dev_1 = Employee('Corey','Schafer', 50000)
dev_2 = Developer('Test', 'User', 50000, "Java")

# print(dev_1.email)
# print(dev_1.pay)

# print(dev_2.email)
# print(dev_2.pay)
# print(dev_2.prolang)

# dev_1.apply_raise()
# dev_2.apply_raise()

# print(dev_1.pay)
# print(dev_2.pay)
# print(help(Developer))

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
            
dev_1 = Developer('Corey','Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 50000, "Java")

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1, dev_2])

print(mgr_1.email)
mgr_1.print_emps()