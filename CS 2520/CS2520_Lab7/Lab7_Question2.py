'''
Prompt: Complete the Course class by implementing the find_student_highest_gpa() instance method, which returns the Student object with the highest GPA in the course.
Assume that no two students have the same highest GPA.
Given the following:
    The main function for testing the program.
    Class Course represents a course, which contains a list of Student objects as a course roster.
    Class Student represents a classroom student, which has three attributes: first name, last name, and GPA.
'''

class Student:
    def __init__(self, student_stats):
        self.first_name = student_stats[0]
        self.last_name = student_stats[1]
        self.gpa = float(student_stats[2])

    def __str__(self):
        # return string representation of the students with their full name and GPA
        return f"{self.first_name} {self.last_name} ( GPA: {self.gpa} )"

class Course:
    def __init__(self):
        self.roster = dict()

    def add_student(self, student):
        self.roster[student] = student.gpa

    def find_student_highest_gpa(self):
        # find max value in dictionary values and return key value pair
        top_student = max(self.roster, key=lambda student: student.gpa)
        return top_student


def main():
    course = Course()

    # add students to the course (user defined)
    # input example: Henry Nguyen 3.5
    # class_size = 4
    # for i in range(class_size):
    #     testStudent = input("Enter the student and grade: ")
    #     course.add_student(Student(testStudent.split()))

    # add students to the course (programmer defined)
    course.add_student(Student(["Henry", "Nguyen", 3.5]))
    course.add_student(Student(["Brenda", "Stern", 2.0]))
    course.add_student(Student(["Lynda", "Robison", 3.2]))
    course.add_student(Student(["Sonya", "King", 3.9]))

    # find and display the student with the highest GPA
    top_student = course.find_student_highest_gpa()
    print(f"Top student: {top_student}")

if __name__ == "__main__":
    main()
