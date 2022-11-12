# Python Object-Oriented Programming
# Four Pillars of Object-Oriented Programming:
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism


class Employee:
    num_of_employees = 0
    raise_amount = 1.20

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('John', 'Smith', 150000)
emp_2 = Employee('Jane', 'Doe', 175000)


print(Employee.num_of_employees)

# print(emp_1.__dict__)
#
# print(emp_1.pay)
# print(emp_1.raise_amount)1
#
# emp_1.apply_raise()
# print(emp_1.pay)
