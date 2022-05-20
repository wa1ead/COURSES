class HUMAN:  #CLASS
    def info(self):
        print("HELLO")

h1 = HUMAN()  #OBJECT
#ATTRIBUTES:
h1.NAME = input("ENTER NAME: ")
h1.HEIGHT = input("ENTER HEIGHT: ")
h1.WEIGHT = input("ENTER WEIGTH: ")

print("NAME:",h1.NAME)
print("HEIGHT:",h1.HEIGHT)
print("WEIGHT:",h1.WEIGHT)