x=[5, 9, -6, 8, 1, 7, 3.4]
print("list(x) = ", list(x))  #SHOW THE LIST"x"

print("len(x) = ", len(x))  #LENGHT OF THE LIST
print("sum(x) = ", sum(x))  #SUM OF VALUES IN THE LIST

#(INDEX, VALUE)
x1=enumerate(x)
print("list(x1) = ", list(x1))

#SORT INCRIMENT
x2=sorted(x)
print("list(x2) = ", list(x2))

print("all(x) = ", all(x))  #TRUE IF ISN'T ANY 0
print("any(x) = ", any(x))  #FALSE IF ALL IS 0

#REVERSE FROM LAST TO FIRST
y=reversed(x)
print("list(y) = ", list(y))

print(x[slice(4)])  #CUT FROM INDEX 0 TO 4
print(x[slice(2, 5)])  #CUT FROM INDEX 2 TO 5
print(x[slice(1, 7, 2)])  #CUT FROM 1 TO 7 INCREASE BY 2 STEPS

#------------------------------------------------------------------
#CREATE A COPY OF "x" IN "y"
y=x.copy()
print("list(x) = ", list(x))
print("list(y) = ", list(y))

#HOW MANY TIMES 7 REPEATED
print("x.count(7) = ", x.count(7))

x.append(2)  #INSERT NEW VALUE
x.insert(4, 2)  #INSERT NEW VALUE IN INDEX 4
print("list(x) = ", list(x))

#REMOVE VALUE
x.remove(9)
print("list(x) = ", list(x))

#REMOVE VALUE IN INDEX 3
x.pop(3)
print("list(x) = ", list(x))

#INDEX OF VALUE
print("x.index(8) = ", x.index(8))

#ADD LIST "y" in LIST "x"
x.extend(y)
print("list(x) = ", list(x))

#CLEAR THE LIST
x.clear()
print("list(x) = ", list(x))