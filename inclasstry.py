class Student:
    total = 0

    def __init__(self, name):
        self.name = name
        Student.total += 1

s1 = Student("nate")
s2 = Student("sam")
s3 = Student("harry")

print(Student.total)