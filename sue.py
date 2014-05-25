def userForLoop(lst):
    '''
    This function parses out the list that is created for each line in main(). After parsing, it outputs a valid Python
    For-loop to commandOutput.py
    '''
    rangeBegin = lst[-3]
    rangeEnd  = lst[-1]
    iterator = lst[1]

    printedCommand = "for "+ iterator + " in range(" + rangeBegin + ", " + rangeEnd + "):\n"

    commandText = open("commandOutput.py", "a")
    commandText.write(printedCommand)
    commandText.close()

def userPrint(lst):
    '''
    Currently having an issue with this function where it adds a superfluous space to the end of the string to be printed
    out. I know that it's an easy fix, but baby steps. What's worrying me the most is that this function is only good at 
    parsing out string arguments. It is currently not suited to print out arguments that are concatenated. Only use a
    single string at this point in Sue's life.
    '''
    printArgStr = ""
    printArgList = lst[1:]
    for each in printArgList:
        printArgStr = printArgStr + each + " "

    printedOut = "print(" + '"' + printArgStr + '"' + ")"
    commandText = open("commandOutput.py", "a")
    commandText.write(printedOut)
    commandText.close()
    
def tab():
    '''
    This function is simple enough to not worry about. It works fine. It adds a tab of four spaces whenever the input for 
    Sue has a '{' in it.
    '''
    tab = "    "
    commandText = open("commandOutput.py", "a")
    commandText.write(tab)
    commandText.close()

def declare(lst):
    '''
    This is also a pretty straight-forwared function. Basic syntax is as follows:
    declare variable [variableName] as a [data type]
    Sue will parse that input and output a valid Python declaration statement. Variable names follow the same conventions in Sue as they do in
    Python.
    '''
    variableType = 0
    variableName = lst[2]

    if (lst[-1].lower() == "string"):
        variableType = '""\n'
    elif (lst[-1].lower() == "list"):
        variableType = "[]\n"
    elif (lst[-1].lower() == "dictionary"):
        variableType == "{}\n"
    elif (lst[-1].lower() == "integer"):
        variableType = "0\n"
    elif (lst[-1].lower() == "float"):
        variableType = "0\n"

    declaration = variableName + " = " + variableType

    commandText = open("commandOutput.py", "a")
    commandText.write(declaration)
    commandText.close()
    
def main():
    '''
    Here we have the main function, where input is taken from commandInput.txt, and is then split into lists to be parsed
    by the other functions that comprise Sue.
    '''
    commandList = []

    userInput = open("commandInput.txt","r")

    for aline in userInput:
        lineTerminate = False
        while not lineTerminate:
            commandList = aline.split()
            print("commandList is", commandList)
            if (commandList[0].lower() == "iterate"):
                userForLoop(commandList)
            elif(commandList[0].lower() == "print"):
                userPrint(commandList)
            elif(commandList[0].lower() == "declare"):
                declare(commandList)
            elif(commandList[0] == "{"):
                tab()
            lineTerminate = True

main()
