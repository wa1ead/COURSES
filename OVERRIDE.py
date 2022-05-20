class A:  #SUPERCLASS
    def function1(self):
        print("ClassA")

class B(A):  #SUBCLASS
    def function1(self):
        print("ClassB")

class C(A):  #SUBCLASS
    def function1(self):
        print("ClassC")

obj1 = A()
obj2 = B()
obj3 = C()
obj1.function1()
obj2.function1()
obj3.function1()