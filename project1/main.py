import re
import string
from enum import Enum

regex = re.compile(r'\!.*?\!')
STATES = ['Initial State', 'KEYWORD', 'IDENTIFIER', 'SEPARATOR', 'OPERATOR', 'REAL', "UNKOWN"]

def isKeyword(key):
    keywords = {"int", "float", "true", "false", "if", "else", "then", "endif", "while", "whileend", "do", "doend", "for", "forend", "input", "output", "and", "or", "not", "bool"}
    if key in keywords:
        return True
    else:
        return False


def isOperator(key):
    operators = {"*", "+", "=", "/", ">", "<", "%"}
    if key in operators:
        return True
    else:
        return False


def isSeperator(key):
    seperators = {"'", "(", ")", "{", "}", "[", "]", ",", ".", ":", ";", " "}
    if key in seperators:
        return True
    else:
        return False

def  FSM(str):
    currentState = 0
    if isSeperator(str):
        currentState = 3
    elif isOperator(str):
        currentState = 4
    elif isKeyword(str):
        currentState = 1
    elif isReal(str):
        currentState = 5
    elif isID(str):
        currentState = 2
    else:
        currentState = 6

    return currentState

# def doubleCheck(word):
#     # for c in word:
#     #     isSeperator(c)
#     # return True
#     #trying to find seps indexes and use splicing to maintain both sep and word to pass to DFSM or isChecks
#     #could also maybe do a dictionary for eaach seperator so we know to return that specific seperator since using split drops the element
#     #struggling to determine how to do if(var) would prob have to do for c in word and manually go through each element
#     if index = word.find(',') or index = word.find('(') or index = word.find(')'):
#         word = word[:index]
#         sep = word[index:]
#     pass


def isReal(str):
    try:
        float(str)
    except ValueError:
        return False
    return True

def isID(str):
    isValid = False
    if str[0].isalpha():
        for i in range(0, len(str)):
            if (not str[i].isalpha()) and (not str[i].isdigit()) and (not str[i] == '$'):
                isValid = False
                break
            isValid = True
    return isValid

def parseIt(str):
    tempArray = []
    index = 0

    #check if the first index is operator or SEPARATOR
    if isOperator(str[0]) or isSeperator(str[0]):
        tempArray.append(str[0])
        str = str[1:]

    while index < len(str):
        if (isOperator(str[index])) or (isSeperator(str[index])):
            # print(f"we want: {str[:index]}")
            # print(f"we also want: {str[index]}")
            tempArray.append(str[:index])
            tempArray.append(str[index])
            str = str[(index+1):]
            index = 0
            if(len(str) == 0):
                break
        else:
            index = index + 1

    if len(str) != 0:
        tempArray.append(str)

    return tempArray


with open('input.txt', mode='r') as input:
    with open('output.txt', mode='w') as output:
        output.write('TOKENS Lexemes\n')
        for line in input:
            result = regex.search(line)
            if not result:
                # output.write(f'{result} comment\n')
                for word in line.split():
                    if FSM(word) != 6:
                        output.write(f'{STATES[FSM(word)]}\t=\t{word}\n')
                    else:
                        parsedArray = parseIt(word)
                        for index in parsedArray:
                            output.write(f'{STATES[FSM(index)]}\t=\t{index}\n')

            else:
                output.write(f'{result} comment\n')
