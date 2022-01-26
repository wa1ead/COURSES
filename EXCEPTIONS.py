while True: #INFINITE LOOP
    try:
        age=int(input("ENTER YOUR AGE: "))
        print("YOU AGE IS ", age, " YEARS OLD")
        break
    except Exception as ex:
        print("YOU ENTERED A WRONG VALUE")
#-------------------------------------------------
while True: #INFINITE LOOP
    try:
        A=int(input("ENTER NUMBER 1: "))
        B=int(input("ENTER NUMBER 2: "))
        print("DIV = ", A/B)
        break
    except ValueError as ex:
        print("PLEASE, ENTER A NUMBER")
    except ZeroDivisionError as ex:
        print("PLEASE, DON'T DIVIDE BY 0")