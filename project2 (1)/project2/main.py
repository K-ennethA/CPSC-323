#
#
#   Assignment 2
# By: Lorena Macias, Kenneth Aguilar, Bryan Cuevas
#
#

import re
regex = re.compile(r'\!.*?\!')
regex2 = re.compile("%%")
tokenPtr = 0
snip = ""

#reads file into a single line while removing whitespace and comments
def oneLine(inputFile):
    s = ""
    with open(inputFile, mode='r') as input:
        for line in input:
            result = regex.search(line)
            result2 = regex2.search(line)
            if (not result) and (not result2) and not line.isspace():
                    s = s + line
        #remove whitespace
        s = " ".join([x.strip() for x in s])
        s = s.replace(" ", "")
        return s


def moreParse(codeSnip):
    semiCol = codeSnip.find(';')
    equals = codeSnip.find('=') + 1
    snip = codeSnip[equals:semiCol] + "$"
    codeSnip = codeSnip[semiCol+1:]
    #returns the snip and the code after snip
    return snip, codeSnip

def syntaxAnalyzer(code):
    print(f"Code to check: {code}")
    output.write(f"Code to check: {code}\n")
    global tokenPtr
    if E() and code[tokenPtr] == '$':
        print("success")
        output.write(f"Finished\n")

    else:
        output.write(f"FAILED\n")
        output.write(f"{code}\n")
        output.write(f"ERROR: {tokenPtr} {code[tokenPtr]}\n")
        print(code)
        print(f"^ {tokenPtr} {code[tokenPtr]}  -----error")

def forward():
    global tokenPtr
    if tokenPtr < len(snip):
        tokenPtr+=1

def backup():
    global tokenPtr
    global snip
    if tokenPtr > 0:
        tokenPtr-=1

def E():
    if T():
        if Q():
            output.write(f"E -> TQ\n")
            print("E --> TQ")
            return True

def T():
    if F():
        if R():
            output.write(f"T -> FR\n")
            print("T -> FR")
            return True
def Q():
    global snip
    global tokenPtr
    cc = snip[tokenPtr]
    forward()
    if cc == '+' or cc == '-':
        if T():
            if Q():
                output.write(f"Q -> TQ\n")
                print("Q -> TQ")
                return True
    else:
        if cc == ')' or '$':
            backup()
            output.write(f"Q -> eps\n")
            print("Q -> eps")
            return True

def R():
    global snip
    global tokenPtr
    cc = snip[tokenPtr]
    forward()
    if cc == '*':
        if F():
            if R():
                output.write(f"R -> *FR\n")
                print("R -> *FR")
                return True
    else:
        if cc == '+' or ')' or '$':
            backup()
            output.write(f"R -> eps\n")
            print("R -> eps")
            return True

def F():
    global snip
    global tokenPtr
    cc = snip[tokenPtr]
    forward()
    if (cc.isalpha()):
        output.write(f"F -> id\n")
        print("F -> id")
        return True
    else:
        if cc == '(':
            if E():
                if cc == ')':
                    output.write(f"F -> (E)\n")
                    print("F -> (E)")
                    return True

inputFile = input("Name of file you wish to open(do not include ext)?") + ".txt"
outputFile = input("What do you wish to save the file as?") + ".txt"
s = oneLine(inputFile)
with open(outputFile, mode='w') as output:
    snip, s = moreParse(s)
    print(snip)
    print(s)
    tokenPtr = 0
    while(len(s) > 0):
        #use the syntaxAnalyser for each snippet of codeSnip
        syntaxAnalyzer(snip)
        tokenPtr = 0
        snip, s = moreParse(s)
    #don't forget to run syntaxAnalyser on last snippet of code
    syntaxAnalyzer(snip)

    output.write(s)
