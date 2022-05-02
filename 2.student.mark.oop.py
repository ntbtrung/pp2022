"""
nguyễn trịnh bảo trung bi11-275
"""

class Student:
    def __init__(self):
        self.__name = ""
        self.__id = ""
        self.__dob = ""

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getDob(self):
        return self.__dob

    def setId(self, sid):
        self.__id = sid

    def setName(self, name):
        self.__name = name

    def setDob(self, dob):
        self.__dob = dob

    def input(self):
        self.__id = input("Enter student ID: ")
        self.__name = input("Enter student name: ")
        self.__dob = input("Enter student dob: ")

    def __str__(self):
        return f"[{self.getId(): <10}] {self.getName(): <20}: {self.getDob(): <15}"


class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def setId(self, cid):
        self.__id = cid

    def setName(self, name):
        self.__name = name

    def input(self):
        self.__id = input("Enter course ID: ")
        self.__name = input("Enter course name: ")

    def __str__(self):
        return f"({self.getId(): <10}) {self.getName(): <20}"


class Mark:
    def __init__(self, student, course, mark):
        self.__student = student
        self.__course = course
        self.__mark = mark


    def getStudent(self):
        return self.__student

    def getCourse(self):
        return self.__course

    def getMark(self):
        return self.__mark

    def setStudent(self, student):
        self.__student = student

    def setCourse(self, course):
        self.__course = course

    def setMark(self, mark):
        self.__mark = mark

class StudentManagement:
    def __init__(self):
        self.__students = []

    def append(self, student):
        self.__students.append(student)

    def inputCount(self):
        while True:
            count = input("Enter number of students: ")
            return int(count)

    def input(self):
        count = self.inputCount()
        for i in range(0, count):
            s = Student()
            s.input()
            self.append(s)

    def count(self):
        return len((self.__students))

    def print(self):
        print("Printing all students")
        for s in self.__students:
            print(s)


class CourseManagement:
    def __init__(self):
        self.__courses = []

    def append(self, course):
        self.__courses.append(course)

    def inputCount(self):
        while True:
            count = input("Enter number of courses: ")
            return int(count)

    def input(self):
        count = self.inputCount()
        print(f"Enter {count} course information")
        for i in range(0, count):
            c = Course()
            c.input()
            self.append(c)

    def count(self):
        return len((self.__courses))

    def print(self):
        print("Printing all courses")
        for c in self.__courses:
            print(c)

    def select(self):
        self.print()
        courseId = input("Enter course id from the table above: ")
        return courseId

class MarkManagement:
    def __init__(self) -> None:
        self.__marks = []

    def input(self, courseId):
        print(f"We are going to input a mark for student in course {courseId}!")
        studentId = input("- Enter student ID: ")
        mark = float(input("- Enter student mark: "))
        markForStudent = Mark(studentId, courseId, mark)
        self.__marks.append(markForStudent)

    def print(self, courseId):
        print(f"Printing all marks for course {courseId}")
        for mark in self.__marks:
            if mark.getCourse() == courseId:
                print(f"{mark.getStudent()} {mark.getCourse()} {mark.getMark()}")


# enter student count and information
studentManagement = StudentManagement()
studentManagement.input()
studentManagement.print()

# enter course count and information
courseManagement = CourseManagement()
courseManagement.input()
courseManagement.print()

# select course, input mark for students in the given course
markManagement = MarkManagement()
for i in range(0, courseManagement.count()):
    courseId = courseManagement.select()
    for i in range(0, studentManagement.count()):
        markManagement.input(courseId)
        markManagement.print(courseId)