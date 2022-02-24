x={1:"A", 2:"B", 3:"C", 4:"D"}

y=x.copy()  #COPY THE ELEMENTS OF DICT"x" IN DICT"y"

print(x.items())  #ALL THE DICTIONARY
print(x.values())  #ONLY VALUES
print(x.keys())  #ONLY KEYS
print(x.get(3))  #THE VALUE OF INDEX "3"

x.popitem()  #DELETE THE FINAL ELEMENT
x.pop(2)  #DELETE THE ELEMENT WITH KEY "2"
print(dict(x))  #SHOW THE DICTIONARY"x"

x.update({3:"E"})  #CHANGE THE VALUE OF KEY "3"
print(dict(x))

x.clear()  #CLEAR THE DICTIONARY
print(dict(x))

A=['x', 'y', 'z']
B=dict.fromkeys(A, 1)  #CREATE A DICTIONARY"B" FROM LIST"A", AND THE VALUES OF "A" WILL BE THE KEYS OF "B" WITH VALUE "1"
print(dict(B))