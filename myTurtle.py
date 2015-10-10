import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex

def gotopos(tur, x, y):
    degrees = tur.heading()
    position = tur.pos()

    tur.up()

    tur.setheading(-90)
    tur.forward(position[1] - y)

    tur.setheading(0)
    tur.forward(-position[0] + x)

    tur.setheading(degrees)
    print(tur.pos())
    tur.down()

var = 20
gotopos(alex, 200, -200)
while True:
    for i in range(4):
        alex.left(90)             # Tell alex to turn by 90 degrees
        alex.forward(var)          # Complete the second side of a rectangle
    var += 20

wn.mainloop()             # Wait for user to close window
