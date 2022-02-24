x={1, 3, 5, 7, 9}
y={2, 4, 6, 8, 9}
x.add(0)  #ADD ELEMENT TO SET"x"
z=x.copy()  #COPY THE ELEMENTS OF SET"x" IN SET"y"

print("STR1", set(x))  #SHOW THE SET"x"
print("STR2", set(y))
print("STR3", set(z))

print("STR4", x.difference(y))  #DIFFERENCES BETWEEN TWO SET'S
print("STR5", x.intersection(y))  #INTERSECTIONS BETWEEN TWO SET'S

#DELETING ELEMENT
x.discard(3)
x.remove(5)
print("STR6", set(x))

#ADD SET TO ANOTHER ONE
print("STR7", x.union(y))
x.update(z)
print("STR8", set(x))

#CLEAR THE SET
x.clear()
print("STR9", set(x))