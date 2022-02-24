x="HELLO"
print(x.capitalize())  #FIRST CHARACTER UPPERCASE
print(x.title())  #THE SAME
print(x.swapcase())  #CHANGE FROM UPPERCASE TO LOWERCASE OR THE OPPOSITE
print(x.upper())  #CHANGE TO UPPERCASE
print(x.lower())  #CHANGE TO LOWERCASE
print(x.casefold())  #THE SAME
print(x.count('L'))  #HOW MANY 'L' IN THE STRING
print(x.endswith('O'))  #IS THE STRING ENDS BY 'O'?
print(x.index('E'))  #THE INDEX OF CHARACTER 'E'
print(x.find('E'))  #THE SAME

#-----------------------------------------------------------------
print(x.isalpha())  #IS THE "x" ALPHABETIC ?
print(x.isdigit())  #IS THE "x" DIGIT ?
print(x.isidentifier())  #IS THE "x" IDENTIFIER ?
print(x.isupper())  #IS THE "x" UPPERCASE ?
print(x.islower())  #IS THE "x" LOWERCASE ?
print(x.isprintable())  #IS THE "x" PRINTABLE ?
print(x.isnumeric())  #IS THE "x" NUMERIC ?
print(x.replace('LO', 'L'))  #REPLACE 'LO' BY 'L'
print(x.startswith('H'))  #IS THE "x" STARTS WITH 'H' ?
print(x.split('E'))  #SPLIT WHEN FOUNDING 'E'