#NORMAL FUNCTION
def sum(A, B):
    total = A+B
    print("SUM =", total)

#HIGHER ORDER FUNCTION
def HOF(X, Y, Z):
    Z(X, Y)
HOF(4, 5, sum)