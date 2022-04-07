'''
nguyễn trịnh bảo trung bi11-275
'''

def inputStudentCount():
    count = int(input("Enter number of students: "))
    return count


def inputStudentInfo(studentCount):
    # returns a dict of students, id is the key, with info from keyboard
    students = []

    # input info for a student: {id, name, dob}
    for i in range(0, studentCount):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter studen DoB: ")
        student = {
            "id": id,
            "name": name,
            "dob": dob,
            "marks": {}
        }
        students.append(student)

    return students


def inputCourseCount():
    count = int(input("Enter number of courses: "))
    return count


def inputCourseInfo(courseCount):
    # return a list of courses, with info from keyboard
    courses = []

    # input info for a course: {id, name}
    for i in range(0, courseCount):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = {
            "id": id,
            "name": name
        }
        courses.append(course)

    return courses


def inputMark(courseid, students):
    print(f"Enter marks of the course {courseid} for students: ")
    for student in students:
        mark = float(input(f"- Student {student['name']}\n"))
        student['marks'][courseid] = mark

        
def listStudents(students):
    print("\n All students list")
    for student in students:
        print(f"{student['id']:<10} {student['name']: <20} {student['dob']: <15}")

        
def listCourses(courses):
    print("\n All courses list")
    for course in courses:
        print(f"{course['id']: <10} {course['name']: <20}")

        
def selectCourse(courses):
    listCourses(courses)
    courseid = input("Enter course id from the table above: ")
    return courseid


def showMark(courseid, students):
    print(f'\n All marks for the course {courseid}')
    for student in students:
        print(f"{student['name']: <20} {student['marks'][courseid]}")

        
studentCount = inputStudentCount()
students = inputStudentInfo(studentCount)
listStudents(students)

courseCount = inputCourseCount()
courses = inputCourseInfo(courseCount)
listCourses(courses)

courseid = selectCourse(courses)
inputMark(courseid, students)

courseid = selectCourse(courses)
showMark(courseid, students)
