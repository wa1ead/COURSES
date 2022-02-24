A=[8, 'W', "WALID", 75]
def output(x:list):
    print(x[0])
    print(x[1])
    print(x[2])
    print(x[3])

output(A)

#-------------------------------------
A=[2, 'W', "WALID", 1]
def output(x:list, S):
    for i in range(S):
        print(x[i])

output(A ,4)