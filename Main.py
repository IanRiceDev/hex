from codes import *
print("1 = encode")
print("2 = decode")
userSelect = input("Make a selection: ")

if userSelect == "1":
    rawUserInput = input("enter text to encode: ")
    userInput = rawUserInput

    def makeUpperCase():
        global userInput
        userInput = userInput.upper()



    def splitInput():
        global userInput
        userInput = list(userInput)


    makeUpperCase()
    splitInput()

    i = 0

    useroutput = userInput
    userOutputLan = len(useroutput)

    while True:


        i = i + 1
        if i > userOutputLan:
            break
        print(textTohex[useroutput[i - 1]] + " ", end='')
if userSelect == "2":
    rawUserInput = input("enter text to decode: ")
    userInput = rawUserInput

    def stripSpaces():
        global userInput
        userInput = userInput.replace(" ","")



    def splitInput():
        global userInput

        n = 2
        userInput = [userInput[i:i + n] for i in range(0, len(userInput), n)]

    stripSpaces()

    splitInput()

    i = 0

    useroutput = userInput
    userOutputLan = len(useroutput)

    while True:

        i = i + 1
        if i > userOutputLan:
            break
        print(hexTotext[userInput[i - 1]], end='')