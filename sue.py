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

    printedOut = "print(" + '"' + printArgStr + '"' + ")\n"
    commandText = open("commandOutput.py", "a")
    commandText.write(printedOut)
    commandText.close()
    
def tab(count):
    '''
    This function is simple enough to not worry about. It works fine. It adds however many tabs are required for the current scope when a "{" is
    found in Sue source code. Also, integer parameter count is incremented by one whenever Sue sees a "{". count is then decremented by one
    each time Sue finds a "}". Make sure your bracket counts match up with each other, or there will be issues with scope.
    '''
    
    
    tab = "    " * count
    commandText = open("commandOutput.py", "a")
    commandText.write(tab)
    commandText.close()

def declareAssign(lst):
    '''
    This is also a pretty straight-forwared function. Basic syntax is as follows:
    declare variable [variableName] as a [data type]
    Sue will parse that input and output a valid Python declaration statement. Variable names follow the same conventions in Sue as they do in
    Python.
    '''
    variableValue = 0
    variableName = lst[2]

    if (lst[-1].lower() == "string"):
        variableValue = '""'
    elif (lst[-1].lower() == "list"):
        variableValue = "[]"
    elif (lst[-1].lower() == "dictionary"):
        variableValue == "{}"
    elif (lst[-1].lower() == "integer"):
        variableValue = "0"
    elif (lst[-1].lower() == "float"):
        variableValue = "0"
    elif (type(int(lst[-1])) is int):
          variableValue = int(lst[-1])
    #elif (type(lst[-1]) is in
          '''
    2014/5/26: The current goal that I have in mind for line 63 is to have the type lst[-1] be
    evaluated so that a variable can be declared with a value rather than with only initialized with
    a dummy value (like 0 for ints and floats and empty lists/dicts/tuples.) I feel like I'm just starting
    to write error-prone code with these increasingly-complex conditional statments. There has to be
    a better way to right this, or, at least, I surely hope there is. I get the distinct feeling that this is
    not very Pythonic, and I also get the feeling that it just plain isn't very good code. It just _looks_
    messy. For now, though, it does what I want it: I can set any integer value to whatever variable
    I want. I would like to do what I can to clean up this function. Maybe I could split the duties
    that are taken care of in this funtion and divvy them out to other functions, or maybe that will
    just be another avenue for error-prone code.

    Another goal is to implement a way for variables to be manipulated as objects (such as using
    variable values as iterables. I would ilke there to be a way to pass a variable holding an iterable
    value like a list to a for loop. I will need to meditate on this some more, but for now, I need sleep.

    declaration = variableName + " = " + str(variableValue) + "\n"

    commandText = open("commandOutput.py", "a")
    commandText.write(declaration)
    commandText.close()


    '''
    
def main():
    '''
    Here we have the main function, where input is taken from commandInput.txt, and is then split into lists to be parsed
    by the other functions that comprise Sue.
    '''
    commandList = []

    userInput = open("commandInput.txt","r")

    tabCount = 0

    '''
    Integer variable tabCount will be incremented by one each time there is a "{" in the Sue source code. The value
    of tabCount will correspond to the amount of tabs required at the point in the code one is at.

    '''

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
                declareAssign(commandList)
            elif(commandList[0] == "{"):
                tabCount += 1
                tab(tabCount)
            elif (commandList[0] == "}"):
                tabCount -= 1
            lineTerminate = True

    print(tabCount)

main()
