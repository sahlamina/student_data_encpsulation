# create a class
class Student_Data:

    #  give it some methods and attributes
    def __init__(self, name, age=24):
        self.name = name
        self._age = age

    def study(self):
        print(self.name + " is studying")

    def online(self):
        print(self.name + " is online")

# call methods and attributes
student = Student_Data("Student", 24)
student.study()
student.online()
print(student._age)


class Student_Data():
    def __init__(self):
        self.name = "student"
        self.__age = 24


stu = Student_Data()
# can be accessed
print(stu.name)
# cannot be accessed
print(stu.__age)
