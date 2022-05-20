def function1():
    print("HELLO WORLD1")
lambda1=lambda :print("HELLO WORLD1")

function1()
lambda1()

#------------------------------------------
def function2(x):
    print(x*x)
lambda2=lambda x:print(x*x)

print(function2(3))
lambda2(3)

#------------------------------------------
def function3():
    return("HELLO WORLD2")
lambda3=lambda :"HELLO WORLD2"

function3()
lambda3()

#------------------------------------------
def function4(x):
    return(x*x)
lambda4=lambda x:x*x

print(function4(5))
lambda4(5)