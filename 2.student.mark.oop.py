
class Student:
    def __init__(self, name, ID, marks1, marks2):
        self.name = name
        self.ID = ID
        self.marks1 = marks1
        self.marks2 = marks2

    def accept(self, name, ID, marks1, marks2):
        ob = Student(name, ID, marks1, marks2)
        ls.append(ob)

    def display(self, ob):
        print("Name : ", ob.name)
        print("ID : ", ob.ID)
        print("C course : ", ob.marks1)
        print("Python course : ", ob.marks2)
        print("\n")

ls = []
obj = Student('', 0, 0, 0)

obj.accept("Paul", 1, 100, 100)
obj.accept("Chris", 2, 90, 90)
obj.accept("Jake", 3, 80, 80)

print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])
