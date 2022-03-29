
class Student:
    def __init__(self, name, ID, dob, marks1, marks2):
        self.name = name
        self.ID = ID
        self.dob = dob
        self.marks1 = marks1
        self.marks2 = marks2

    def accept(self, name, ID, dob, marks1, marks2):
        ob = Student(name, ID, dob, marks1, marks2)
        ls.append(ob)

    def display(self, ob):
        print("Name : ", ob.name)
        print("ID : ", ob.ID)
        print("D.O.B : ", ob.dob)
        print("C course : ", ob.marks1)
        print("Python course : ", ob.marks2)
        print("\n")

ls = []
obj = Student('', 0, 0, 0)

obj.accept("Paul", 1,  24-11-2002, 100, 100)
obj.accept("Chris", 2, 20-10-2001, 90, 90)
obj.accept("Jake", 3, 18-08-1999, 80, 80)

print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])
