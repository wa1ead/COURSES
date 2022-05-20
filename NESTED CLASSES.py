class A:
    x:int
    def myFun1(self):
        print("NumberA =",self.x)
    
    class B:
        y:int
        def myFun2(self):
            print("NumberB =",self.y)

b = A.B()
b.y = 11
b.myFun2()
