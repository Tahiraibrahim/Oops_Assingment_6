# 06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Assingment-1

# Create a class Student with attributes name and marks.
#  Use the self keyword to initialize these values via a constructor.
#  Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 

    def display(self):
        print(f"Student Nmae: {self.name}")
        print(f"Marks: {self.marks}")


student1 = Student("Tahira Ibrahim", 90)
student1.display()
        