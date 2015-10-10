import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()

# print('what do you want to make?')
# make = input('> ')

def makeFlower():
    print('making a flower')

def makeLeaf(tur, size):

    tur.right(45)
    tur.forward(size)
    for i in range(270):
        tur.right(1)
        tur.forward(size / 60)
    tur.forward(size)

    window.mainloop()



options = {
    'flower': makeFlower,
    'leaf': makeLeaf
}

# try:
#     options[make]()
# except KeyError:
#     print('we can\'t make a '+make)

makeLeaf(alex, 90)
