class Person:
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

class Student(Person):
    def myFun(self):
        print("HELLO STUDENT")

obj1 = Student("WALID", 19)
print("MY NAME IS :",obj1.name," AND MY AGE IS :",obj1.age)
