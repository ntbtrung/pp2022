#nguyen trinh bao trung bi11-275 labwork 1
y = dict()
b = dict()

n = int(input("Number of students:"))

for i in range(0, n):
    x = input("Enter the student name: ")
    z = input("Enter the student ID: ")
    m = input("Enter the student birthday: ")
    y[i] = dict(name = x, id = z, dob = m)

for i in range(0, n):
    print(y[i])

a = int(input("Number of courses:"))

for j in range(0, a):
    t = input("Enter the course name:")
    v = input("Enter the course ID:")
    b[j] = dict(course_name = t, id = v )

for i in range(0, n):
    c = str(input('Select course:'))
    for j in range(0, a):
        if c == b[j]['course_name']:
            y[i]['course infor'] = b[j]
            y[i]['course mark'] = int(input("Enter mark:"))

for j in range(0, a):
    print(b[j])

for i in range(0, n):
    print(y[i])