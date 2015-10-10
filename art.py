import turtle             # Allows us to use turtles
import math
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()

print('what do you want to make?')
make = input('> ')

def makeFlower(tur):
    print('making a flower')
    for j in range(20):
        for i in range (2):
            tur.forward(25)
            tur.left(45)
            tur.forward(25)
            tur.left(45*3)
        tur.left(360/20)

def makeLeaf(tur, size):

    tur.right(45)
    tur.forward(size)
    for i in range(270):
        tur.right(1)
        tur.forward(size / 60)
    tur.forward(size)

    wn.mainloop()



options = {
    'flower': makeFlower,
    'leaf': makeLeaf
}

try:
    options[make](alex)
except KeyError:
    print('we can\'t make a '+make)
