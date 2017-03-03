import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("HEX")
from hexCodes import *

while True:

    print("1 = Encode")
    print("2 = Decode")
    print("3 = Exit")
    userSelect = input("Make a selection: ")

    if userSelect == "1":
        rawUserInput = input("Enter text to encode: ")
        userInput = rawUserInput




        def splitInput():
            global userInput
            userInput = list(userInput)



        splitInput()

        i = 0

        useroutput = userInput
        userOutputLan = len(useroutput)

        while True:
            if i == userOutputLan:
                break
            try:
                print(textToHex[useroutput[i]] + " ", end='')

            except KeyError:
                print("One of the char in the string is not a char that can be turned in to hex")
                break

            i = i + 1


        print(" ")
        print("-----------------------------")

    if userSelect == "2":
        from hexCodes import *
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

            if i == userOutputLan:
                break
            try:
                print(hexToText[useroutput[i]], end='')

            except KeyError:
                print("One of the char in the string is not a char that can be turned in to text")


            i = i + 1

        print(" ")
        print("-----------------------------")

    if userSelect == "3":
        break

    userSelectList = ["1","2","3"]

    if userSelect not in userSelectList:
        print("Please make a possible selection")
        print(" ")
        print("-----------------------------")