'''
Implement a superclass Person. Make two classes, Student and Instructor, that inherit from Person.
A person has a name and a year of birth. A student has a major, and an instructor has a salary.
Write the class declarations, the constructors, and the __repr__ method for all classes.
Supply a test program that tests these classes and methods
'''

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __repr__(self):
        return f'Name: {self.name} \
            \n  Stats: Born in {self.birth_year}.'


class Student(Person):
    def __init__(self, name, birth_year, major):
        super().__init__(name, birth_year)
        self.major = major

    def __repr__(self):
        return f'{super().__repr__()} Is a student majoring in {self.major}.'


class Instructor(Person):
    def __init__(self, name, birth_year, salary):
        super().__init__(name, birth_year)
        self.salary = salary

    def __repr__(self):
        return f'{super().__repr__()} Is a professor earning a salary of ${self.salary}.'


# main method to test these classes and methods
def main():
    # create instances of a person and student and instructor
    person = Person("Jonathan Apple", 1748)
    student = Student("Connor McCarry", 2001, "Computer Science")
    instructor = Instructor("Professor Professorson", 1969, 120000)

    # display instance information
    print(f'{person} \n{student} \n{instructor}')

if __name__ == "__main__":
    main()
    