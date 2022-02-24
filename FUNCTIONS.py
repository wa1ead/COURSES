def sum(A, B):  #DEFINING A FUNCTION
    return A+B

print(sum(15, 25))  #VALUES BETWEEN BRACKETS ARE PARAMETERS

#-------------------------------------------------------------
def info(name, age):
    print("NAME =", name)
    print("AGE =", age)

info(input("ENTER YOUR NAME: "), int(input("ENTER YOUR AGE: ")))