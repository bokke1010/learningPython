print('what do you want to make?')
make = input('> ')

def makeFlower():
    print('making a flower')

options = {
    'flower': makeFlower
}

try:
    options[make]()
except KeyError:
    print('we can\'t make a '+make)
