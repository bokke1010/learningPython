import python

secretPassword = "hello"
lastError = False
tries = 1
while True:
    if lastError:
        typedPassword = input("wrong pass, try again: ")
        tries = tries =+ 1
    else:
        typedPassword = input("password: ")

    if typedPassword == secretPassword:
        print('Access granted')
        fibonatie(tries)
        break
    elif typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage.')
        lastError = True
    else:
        print('Access denied')
        lastError = True
