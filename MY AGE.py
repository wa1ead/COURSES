import datetime
birthyear = int(input("enter your birthyear: "))
age = datetime.datetime.now().year - birthyear
print("YOUR AGE IS", age, "YEARS OLD")