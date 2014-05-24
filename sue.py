def userForLoop(lst):
    rangeBegin = lst[-3]
    rangeEnd  = lst[-1]
    iterator = lst[1]

    printedCommand = "for "+ iterator + " in range(" + rangeBegin + ", " + rangeEnd + "):\n"
    print("printedCommand is", printedCommand)

    commandText = open("command.py", "a")
    commandText.write(printedCommand)
    commandText.close()

def userPrint(lst):
    '''
    The main problem that I'm facing with this function is that it doesn't format string arguments
    correctly when they are larger than a single string. I also need to eventually implement a way
    for this userPrint function to concatenate arguments.
    '''
    printArgStr = ""
    printArgList = lst[1:]
    for each in printArgList:
        printArgStr = printArgStr + each + " "
    print(printArgStr)
        

    
    printedOut = "print(" + '"' + printArgStr + '"' + ")"
    commandText = open("command.py", "a")
    commandText.write(printedOut)
    commandText.close()
    
def tab():
    tab = "    "
    commandText = open("command.py", "a")
    commandText.write(tab)
    commandText.close()
    


def main():
    commandList = []

    userInput = open("commandInput.txt","r")

    for aline in userInput:
        lineTerminate = False
        while not lineTerminate:
            commandList = aline.split()
            print("commandList is", commandList)
            if (commandList[0] == "iterate"):
                userForLoop(commandList)
            elif(commandList[0] == "print"):
                userPrint(commandList)
            elif(commandList[0] == "{"):
                tab()
            lineTerminate = True


    

    if (commandList[0] == "end"):
        return False
    else:
        return True
programming = True

def control():
    while programming:
        main()
        if main() == False:
            programming = False


main()
