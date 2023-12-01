class Animal:
    c = 0
    def count(self):
        self.c = self.c + 1
        print(self.c, 'animals')

animal = Animal()
animal.count()
animal.count()
print(type(animal))

class Student:
    num = 0
    name = ''
    def __init__(self, nam: str):
        self.name = nam
        print(self.name, 'constructed')
        # pass
    
    def number(self):
        self.num = self.num + 2
        print(self.name, self.num)

    # def __del__(self):
    #     print(self.name, 'Student record deleted')

st = Student('James')
pr = Student('Peter')

st.number()
pr.number()
# st = 'change string'
# print('st contains:', st)

# Inheritance
class Subject(Student):
    grade = 0
    def grades(self):
        self.grade = self.grade + 5
        print(self.name, self.grade, 'points')

sam = Subject('Samuel')
sam.number()
sam.grades()

