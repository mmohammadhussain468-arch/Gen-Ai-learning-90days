class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.course=course
        self.age=age

    def show_details(self):
        print("Name:",self.name)
        print("course:",self.course)
        print("age:",self.age)

name=input("Enter ur name:")
course=input("Enter ur course:")
try:
    age=int(input("enter ur age:"))
except ValueError:
    print("invalid age")
    age=0


student = Student(name, age, course)
student.show_details()


with open("name.txt","w") as file:
    file.write("Name: " + student.name + "\n")
    file.write("Age: " + str(student.age) + "\n")
    file.write("Course: " + student.course + "\n")


with open("name.txt", "r") as file:
    print("\nSaved Details:")
    print(file.read())