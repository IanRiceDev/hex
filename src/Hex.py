import pprint
while True:
    from hexCodes import *
    print("1 = Encode")
    print("2 = Decode")
    print("3 = Exit")
    userSelect = input("Make a selection: ")

    if userSelect == "1":
        rawUserInput = input("enter text to encode: ")
        userInput = rawUserInput




        def splitInput():
            global userInput
            userInput = list(userInput)



        splitInput()

        i = 0

        useroutput = userInput
        userOutputLan = len(useroutput)

        while True:


            i = i + 1
            if i > userOutputLan:
                break
            print(textToHex[useroutput[i - 1]] + " ", end='')
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

            i = i + 1
            if i > userOutputLan:
                break
            print(hexToText[useroutput[i - 1]], end='')
        print(" ")
        print("-----------------------------")
    if userSelect == "3":
        break
