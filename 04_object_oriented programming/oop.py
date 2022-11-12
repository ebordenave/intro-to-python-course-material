# Python Object-Oriented Programming
# Four Pillars of Object-Oriented Programming:
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith', 150000)
emp_2 = Employee('Jane', 'Doe', 175000)

print(emp_2.fullname())
