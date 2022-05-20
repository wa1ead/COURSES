class A: #SUPER CLASS
    age:int
    def info(self):
        self.age = 10
        print("AGE: ", self.age)

class B(A): #SUB CLASS
    def info2(self):
        super().info()

b1 = B()
b1.info2()
