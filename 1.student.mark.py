#nguyen trinh bao trung bi11-275 labwork 1
def inputStudentCount():
    count = int(input("Enter number of students: "))
    return int(count)

def inputStudentInfo(studentCount):
    # returns a dict of students, id is the key, with info from keyboard
    students = {}

    #input info for a student: {id, name, dob}
    for i in range(0, studentCount):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter studen DoB: ")
        students[id] = {
            "name": name,
            "dob": dob,
            "marks": {}
        }

    return students

def inputCourseCount():
    count = int(input("Enter number of courses: "))
    return count

def inputCourseInfo(courseCount):
    #return a list of courses, with info from keyboard
    courses = {}

    #input info for a course: {id, name}
    for i in range(0, courseCount):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses[id] = name

    return courses

def inputMark(coursesid, students):
    print(f"Enter marks of the course {coursesid} for students: ")
    for id in students:
        mark = float(input(f"- Student {students[id]['name']}"))
        students[id]['marks'][coursesid] = mark

def listCourses(courses):
    print("\n All courses list")
    for id in courses:
        print(f"{id: <10} {courses[id]: <20}")

def selectCourse(courses):
    listCourses(courses)
    coursesid = input("Enter course id from the above table: ")
    return coursesid

def listStudents(students):
    print("\n All students list")
    for id in students:
        print(f"{id:<10} {students[id]['name']: <20} {students[id]['dob']: <15}")

def showMark(coursesid, students):
    print("\n All marks for the course {coursesid}")
    for id in students:
        print(f"{students[id]['name']: <20} {students[id]['mark'][coursesid]}")

#enter student count and information
studentCount = inputStudentCount()
students = inputStudentInfo(studentCount)
listStudents(students)

#enter course count and information
courseCount = inputCourseCount()
courses = inputCourseInfo(courseCount)
listCourses(courses)

#select course, input mark for students in the given courses
coursesid = selectCourse(courses)
inputMark(coursesid, students)

#show marks for a given course
coursesid = selectCourse(courses)
showMark(coursesid, students)
