'''
Make a class Employee with a name and salary.
Make a class Manager inherit from Employee.
Add an instance variable, named _department, that stores a string.
Supply a method __repr__ that prints the manager's name, department, and salary.
Make a class Executive inherit from Manager.
Supply appropriate __repr__ methods for all classes.
Supply a test program that tests these classes and methods.
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f'Name: {self.name} \
                \n  Stats: Salary of ${self.salary}'


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def __repr__(self):
        return f'{super().__repr__()}, Manger at the Department of {self._department}'


class Executive(Manager):
    def __repr__(self):
        return f'{super().__repr__()} and Executive'

# main method to test these classes and methods
def main():
    # create instance of an employee and manager and executive
    employee = Employee("John Wick", 5000000)
    manager = Manager("Jonny Wick", 123456, "Technicians")
    executive = Executive("Jonathan Wick", 15000, "Marketing")

    # display instance information
    print(f'{employee} \n{manager} \n{executive}')

if __name__ == "__main__":
    main()
    