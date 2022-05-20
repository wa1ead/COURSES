def add(A):
    if A != 0:
        return A + add(A-1)
    else:
        return 0

x=int(input("ENTER A NUMBER: "))
print("SUM = ", add(x))