import turtle             # Allows us to use turtles
import math
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()

# print('what do you want to make?')
# make = input('> ')

def makeFlower():
    print('making a flower')

def drawLeaf(tur, size, degrees):

    tur.right(degrees / 2)
    tur.forward(size)
    for i in range(270):
        tur.left(1)
        tur.forward((size * math.pi) / (degrees * 90))
    tur.forward(size)

    wn.mainloop()



options = {
    'flower': makeFlower,
    'leaf': drawLeaf
}

# try:
#     options[make]()
# except KeyError:
#     print('we can\'t make a '+make)
alex.setheading(0)
drawLeaf(alex, 90, 45)
