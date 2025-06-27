# Partially Implemented Abstract Class
# Instructions:
# Create an abstract class named Employee:
# Abstract method: calculate_salary().
# Concrete method: display_role() (prints role).
# Create concrete classes:
# FullTimeEmployee with a calculate_salary() method.
# PartTimeEmployee with a calculate_salary() method.
# Instantiate both and test both methods.


from abc import ABC, abstractmethod

class Employee(ABC):
    def display_role(self):
        print("Employee role")

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Full-time salary: 50000")

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("Part-time salary: 20000")

full_time = FullTimeEmployee()
part_time = PartTimeEmployee()

full_time.display_role()
full_time.calculate_salary()

part_time.display_role()
part_time.calculate_salary()
